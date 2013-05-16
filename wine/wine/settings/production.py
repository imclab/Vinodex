DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cse110_dev', # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'cse110app',
        'PASSWORD': 'apppass',
        'HOST': 'ec2-54-225-44-160.compute-1.amazonaws.com', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432', # Set to empty string for default.
    }
}
