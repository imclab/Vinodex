import os
from base import *

ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT")

if ENVIRONMENT == "production":
    from production import *
elif ENVIRONMENT == "test":
    from test import *
else:
    from development import *
