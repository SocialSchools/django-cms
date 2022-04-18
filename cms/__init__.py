# import django
# this break when we are installing via github, we will switch to the one from pypi
# from 3.11.0
__version__ = '3.10.3'

# if django.VERSION < (3, 2):
default_app_config = 'cms.apps.CMSConfig'
