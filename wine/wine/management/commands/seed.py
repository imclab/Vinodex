from wine.jobs import WineDataJob
import requests
from django.core.management.base import BaseCommand
from wine.models import Wine, Winery

class Command(BaseCommand):
    args = '<filename>'
    help = 'Seeds the wine database from the given wine data file'
    def handle(self, *args, **options):
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

        filename = None
        if not args:
            filename = 'wine_dotcom_api_data'
        else:
            filename = args[0]

        try:
            open(filename)
        except IOError:
            filename = 'wine_dotcom_api_data'
            print "Could not open wine data file"
            print "Downloading the wine file, this will take a while"
            response = requests.get("http://zackg.me/wine_dotcom_api_data")
            response.raise_for_status()
            with open(filename,'w') as write_handle:
                write_handle.write(response.content)

        print "Starting wine data job"
        WineDataJob().process(filename)
        print "Seed complete"
