==========
Do Not Use 
==========

This is an unstable project in development. Please do not use. 


Installation
============

Clone this repo and install the requirements into your virtualenv:
    git clone https://github.com/cartwheelweb/exampledjangoshop
    mkvirtualenv exampledjangoshop
    workon exampledjangoshop
    cd exampledjangoshop
    pip install -r requirements/project.txt

Make a directory called 'build' and clone the cartwheelweb fork of the django-shop repo into it:
    mkdir build
    cd build
    git clone git@github.com:cartwheelweb/django-shop.git

Then install django-shop:
    cd django-shop
    python setup.py install
    cd ../..

In settings.py, replace the line in TEMPLATE_DIRS like this with the correct absolute path:
    '/home/scaredofrabbits/code/exampledjangoshop/build/django-shop/shop/templates'
(TODO: automatically set the correct path here)

Then syncdb and run:
    python manage.py syncdb
    python manage.py runserver

