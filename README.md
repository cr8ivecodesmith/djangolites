Lightweight Django Chapter Excercises
=====================================

#### Setting up

I'm using python 3 for this book.

    mkvirtualenv --python=/usr/bin/python3 --no-site-packages djangolites
    setvirtualenvproject
    pip install -r requirements.pip

Note that I'm running through a VM with an IP of `192.168.56.32` so all my run server commands
will be run through that address so I can access it through my local.


## Chapter 1 - World's Smallest Django Project

All you need is a single file with the most minimum settings, a view, and a url pattern.


Running for development:

    python hello.py runserver 192.168.56.32:8000


Running through gunicorn:

    gunicorn hello --bind=192.168.56.32:8000 --log-file=-


Running with debug off (production):

    export DEBUG=off
    export ALLOWED_HOSTS=localhost,example.com


Creating a reusable template off of this single file Django app is easy too. Keep in mind of the
context variables used when a Django project is created from a template:

* `project_name`
* `project_directory`
* `secret_key`
* `docs_version`

With that I've created a `litestart` template from this:

    django-admin.py startproject peanut_butter --template=litestart

This will create a project named `peanut_butter`.

