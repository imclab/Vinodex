import requests
import random
from django.core.management.base import BaseCommand
from wine.models import UserProfile, Cellar, Wine, Bottle

class Command(BaseCommand):
    args = '<profile_id, num_cellars, min_bottles_per_cellar, max_bottles_per_cellar>'
    help = 'Create cellars for a given user, populated with some bottles'
    def handle(self, *args, **options):
        if not Wine.objects.exists():
            raise ValidationError("There are no wines in the database, you may"
                    "want to seed it first")

        profile_id, num_cellars, min_bottles_per_cellar, max_bottles_per_cellar =\
            [int(arg) for arg in args]
        
        profile = UserProfile.objects.get(id=profile_id)
        for cellar_idx in range(num_cellars):
            cellar = Cellar.objects.get_or_create(name = "Cellar%d" % cellar_idx,
                                                  location = "Spot%d" % cellar_idx,
                                                  owner = profile)[0]
            num_bottles = int(random.uniform(min_bottles_per_cellar,max_bottles_per_cellar))
            for bottle_idx in range(num_bottles):

                # This is a slow query, but it's okay because this is just a
                # seeding command
                wine = Wine.objects.order_by('?')[0]
                bottle = Bottle.objects.create(wine=wine,cellar=cellar)
