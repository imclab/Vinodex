from wine.models import Sommelier
from wine.jobs import SommelierDataJob
from django.core.management import BaseCommand
class Command(BaseCommand):
    args = '<sommeilier_data_file>'
    help = 'Generates the sommeilier data from the sommeilier data file'
    def handle(self, *args, **options):
        if not args:
            raise ValueError("A Sommelier data file is required")
        file_handle = open(args[0])

        Sommelier.objects.all().delete()
        SommelierDataJob(file_handle).process()
