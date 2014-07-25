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
