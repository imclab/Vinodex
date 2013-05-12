from wine.jobs import WineDataJob
import requests
from django.core.management.base import NoArgsCommand
from wine.models import Wine, Winery

class Command(NoArgsCommand):
    def handle_noargs(self, *args, **options):
        print "About to seed the database..."
        print("Do you want me to remove all wines and wineries from the database "
        "first? (y/n)")
        response = raw_input()
        if response[0] == 'y' or response[0] == 'Y':
            print "Okay, truncating the tables"
            Wine.objects.all().delete()
            Winery.objects.all().delete()
        else:
            print "Okay, I'll leave the database intact"

        print "This is going to take a while, go grab some coffee"
        try:
            open('wine_dotcom_api_data')
        except IOError:
            print "Downloading the wine file"
            response = requests.get("http://zackg.me/wine_dotcom_api_data")
            response.raise_for_status()
            with open('wine_dotcom_api_data','w') as write_handle:
                write_handle.write(response.content)

        print "Starting wine data job"
        WineDataJob().process('wine_dotcom_api_data')
        print "Seed complete"
