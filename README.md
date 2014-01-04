Running the server
------------------

You should run the server in a virtualenv. This can be done like so:

    pip install virtualenv
    virtualenv venv
    
Whenever you wish to work on the project, just cd into the directory that you ran the
`virtualenv venv` command, and run
    
    source venv/bin/activate
    

Then, you should install the requirements for the project:

    pip install -r requirements.txt

You will also need to install the tesseract OCR library. On Mac OS X,
this can be done like so:

    brew install tesseract

You will also need to install the zxing library. You should probably be able
to install it this way (you may need to be logged in as root):

    wget http://zxing.googlecode.com/files/ZXing-1.6.zip
    unzip -d /opt/local/
    cd /opt/local/zxing-1.6 
    ant -f core/build.xml
    ant -f javase/build.xml

Finally, you can run the server like so:

    cd wine
    python manage.py runserver

Database Setup
---------------

We require a Postgresql database with the postgis extension installed.

On OS X `postgis` can be installed by running the commands:

    brew install postgis
    initdb /usr/local/var/postgres

After creating your database, run

    CREATE EXTENSION postgis;

on the database.

Finally, you can run the migrations:

    python wine/manage.py syncdb
    python wine/manage.py migrate wine


Populating the Database with sample data
----------------------------------------

If you want, you can populate your database with wines gathered from
the wine.com API. This is necessary for Label and barcode recognition to work
successfully. It will also be helpful for autocomplete. You can seed the database
like so:

    cd wine
    python manage.py seed


    
Testing
-------

You should test your code before sumbitting a pull request.

To test your code, use the following command:

    python manage.py test wine
    
    
If you wish to add tests to the code, our tests are in the `tests` directory. You should
add new tests whenever you implement new functionality.

BUMP
