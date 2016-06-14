# The Leaky Cauldron
-------------------------------------------------
A minimalistic blog, powered by Django made on Python 3.4.

Requirements
============
Install the following if you haven't already :
    $ pip install Pillow
    $ pip install mysqlclient (if using mysql database)
    $ pip install sorl-thumbnail

Installation
============
Installation on localhost
- Clone this Repository
- Open settings.py from theleakycauldron folder.
- Edit your database details
- make migrations
    $ python manage.py makemigrations blog
    $ python manage.py makemigrations thumbnail
    $ python manage.py migrate
- create super user
    $ python manage.py createsuperuser
- run the wsgi server
    $ python manage.py runserver
- goto localhost:8000/admin from your browser, log in using your super user credentials and enter the user details first name and last name
- goto localhost:8000 on browser and you are live


Questions or Suggestions?
=========================
Follow me on `twitter` @vaibhaved : http://twitter.com/vaibhaved

`live example`: http://theleakycauldron.pythonanywhere.com