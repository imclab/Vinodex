import requests
import pickle
from wine.models import Wine, Winery, Sommelier
from django.db import IntegrityError, transaction

class SommelierDataJob(object):

    def __init__(self, handle):
        self.handle=handle

    @staticmethod
    def is_food(line):
        return line[0] != '-'

    @staticmethod
    def parse_food(line):
        return line.strip()

    @staticmethod 
    def parse_wine(line):
        wine = line[1:].strip() 
        comment = None
        pronounce = None
        pronounce_start, pronounce_end = line.find("("), line.find(")")
        comment_start, comment_end = line.rfind("("), line.rfind(")")

        if pronounce_start != -1 and pronounce_end != -1:
            wine = line[1:pronounce_start].strip()
            pronounce = line[pronounce_start+1:pronounce_end].strip()

        if (comment_start != -1 and comment_end != -1 and comment_start != pronounce_start):
            comment = line[comment_start+1:comment_end].strip()

        return wine, pronounce, comment


    def process(self):
        food = None
        for line in self.handle.readlines():
            print line
            if (line.isspace()):
                continue
            elif (self.is_food(line)):
                food = self.parse_food(line)
            else:
                wine, pronounce, comment = self.parse_wine(line)
                Sommelier.objects.get_or_create(wine_type = wine,
                                         pairing = food,
                                         comment = comment,
                                         pronounce = pronounce)

class WineDataJob(object):
    """
        This job queries the Wine.com API for their first 50000 wines.
        Note that we are actually limited to 1000 API queries per day on 
        the provded API key
    """
    APIKEY ="e45f4f430bfbeef004461424b26e3859"
    API_URL =\
    "http://services.wine.com/api/beta2/service.svc/json/catalog?sortby=popularity%7Cdescending"
    LIMIT = 100
    
    @staticmethod
    def get_data(limit, offset):
        url = WineDataJob.API_URL + "&size=%d&offset=%d&apikey=%s" % (limit,
                offset, WineDataJob.APIKEY)
        print "Querying:", url
        response = requests.get(url)
        if response.status_code != 200:
            throw ("Invalid status code: %d" % response.status_code)
        return response.json()["Products"]["List"]
       
    def __init__(self, offset = 0):
        self.initial_offset = offset

    @staticmethod
    def location_data_valid(location_data):
        return (location_data["Latitude"] != -360 and
                location_data["Longitude"] != -360)

    @staticmethod
    def get_winery_location(winery_location):
        if winery_location is not None and WineDataJob.location_data_valid(winery_location):
            return PointField(winery_location["Longitude"],
                    winery_location["Latitude"])
        else:
            return None

    @staticmethod
    def create_winery(winery_data):
        url = winery_data.get("Url")
        name = winery_data["Name"]
        location = WineDataJob.get_winery_location(winery_data.get("GeoLocation"))
        winery = Winery(name = name, url = url, location = location)
        winery.save()
        return winery

    @staticmethod
    def find_existing_winery(winery_data):
        url = winery_data.get("Url")
        if url is not None:
           existing_wineries = Winery.objects.filter(url=url) 
           if existing_wineries:
               return existing_wineries[0]
           else:
               return None
        else:
            return None

    @staticmethod
    def get_winery_info(winery_data):
        if winery_data is not None:
            existing_winery = WineDataJob.find_existing_winery(winery_data)
            if existing_winery:
                return existing_winery
            else:
                return WineDataJob.create_winery(winery_data)
        else:
            return None

    @staticmethod
    def extract_name_and_vintage(wine_name):
        chunks = wine_name.split()
        name_chunks = [chunk for chunk in chunks if not chunk.isdigit()]
        vintage_chunks = [chunk for chunk in chunks if chunk.isdigit()]
        name = " ".join(name_chunks)
        if vintage_chunks:
            return name, vintage_chunks[0]
        else:
            return name, None

    @staticmethod
    def extract_photo_url(wine_labels):
        if wine_labels:
            return wine_labels[0].get("Url")
        else:
            return None

    @staticmethod
    def extract_wine_type(varietal):
        if varietal:
            return varietal.get("Name")
        else:
            return None

    @staticmethod
    def extract_wine_color(varietal):
        if varietal and varietal.get("WineType"):
            return varietal["WineType"].get("Name")
        else:
            return None

    @staticmethod
    def extract_price(price):
        if price is not None:
            return int(price*100.0)
        else:
            return None

    @staticmethod
    def validate_prices(min_price, max_price, retail_price):
        if min_price is not None and max_price is not None and min_price > max_price:
            return min_price, min_price, min_price
        if retail_price is not None and max_price is not None and retail_price > max_price:
            return retail_price, retail_price, retail_price
        if retail_price is not None and min_price is not None and retail_price < min_price:
            return retail_price, retail_price, retail_price
        return min_price, max_price, retail_price

    @staticmethod
    def get_wine_info(wine_data):
        name, vintage = WineDataJob.extract_name_and_vintage(wine_data["Name"])
        label_photo = WineDataJob.extract_photo_url(wine_data.get("Labels"))
        wine_type = WineDataJob.extract_wine_type(wine_data.get("Varietal"))
        wine_color = WineDataJob.extract_wine_color(wine_data.get("Varietal"))
        min_price = WineDataJob.extract_price(wine_data.get("PriceMin"))
        max_price = WineDataJob.extract_price(wine_data.get("PriceMax"))
        retail_price = WineDataJob.extract_price(wine_data.get("PriceRetail"))
        min_price, max_price, retail_price =\
        WineDataJob.validate_prices(min_price, max_price, retail_price)
        url = wine_data.get("Url")
        return Wine(name=name,
                    vintage=vintage,
                    wine_type=wine_type,
                    color=wine_color,
                    min_price=min_price,
                    max_price=max_price,
                    retail_price=retail_price,
                    url=url,
                    label_photo=label_photo)

    @staticmethod
    def wine_already_exists(wine):
        if wine.winery:
            return Wine.objects.filter(name=wine.name,vintage=wine.vintage,winery_id
                    = wine.winery.id)
        else:
            return Wine.objects.filter(name=wine.name,vintage=wine.vintage)

    @staticmethod
    def remove_winery_name_from_wine(wine, winery):
        wine.name = wine.name.partition(winery.name)[2].strip()
        return wine

    @staticmethod
    def parse_wine_data(wine_data):
        wine = WineDataJob.get_wine_info(wine_data)
        winery = WineDataJob.get_winery_info(wine_data.get("Vineyard"))
        if winery:
            # The Wine.com API leaves the winery name in the wine 
            # name, so this gets rid of the winery name if it can be
            # found in the wine name
            wine = WineDataJob.remove_winery_name_from_wine(wine, winery)
        return wine, winery

    def download(self, num_entries, filename = "wine_dotcom_api_data"):
        wines = []
        for request_index in range(num_entries / self.LIMIT):
            offset = self.initial_offset + self.LIMIT * request_index
            wines += self.get_data(self.LIMIT, offset)
        file = open(filename, 'w')
        pickle.dump(wines, file)

    def process(self, filename = "wine_dotcom_api_data"):
        file = open(filename)
        print "Loading wines from data file"
        wines = pickle.load(file)
        print "Importing wines into the database"
        for wine_data in wines:
            wine, winery = self.parse_wine_data(wine_data)
            wine.raw_data = wine_data
            if winery is not None:
                winery.raw_data = wine_data.get("Vineyard")
            if not self.wine_already_exists(wine):
                wine.winery = winery
                wine.save()
