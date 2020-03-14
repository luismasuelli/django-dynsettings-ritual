__author__ = 'luismasuelli'
from django.http import HttpResponse
from grimoire.django.dynsettings.utils import settings


def sample(request):
    """
    Sample view. Please declare REQINTEGER as an existing setting in the database to run this sample.
    """
    return HttpResponse("""
    Sample setting: %s, %s
    """ % (getattr(settings, 'REQINTEGER', 3), settings.STATIC_URL))