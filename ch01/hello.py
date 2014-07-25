import sys

from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application
from django.conf.urls import url
from django.http import HttpResponse


##### SETTINGS
settings.configure(
    DEBUG=True,
    SECRET_KEY='supersecretkeykeepitsafe',
    ROOT_URLCONF=__name__,
)
application = get_wsgi_application()
##### END SETTINGS


##### VIEWS
def index(request):
    return HttpResponse('Hello World')
##### END VIEWS


##### URLS
urlpatterns = (
    url(r'^$', index),
)
##### END URLS


if __name__ == '__main__':
    execute_from_command_line(sys.argv)
