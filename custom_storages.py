from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Dummy Tag """
    location = settings.STATICFILES_LOCATION


class Mediatorage(S3Boto3Storage):
    """ Dummy Tag """
    location = settings.MEDIAFILES_LOCATION