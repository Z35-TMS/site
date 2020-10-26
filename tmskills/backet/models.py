from django.db import models
from user.models import TmsUser


class Bucket(models.Model):

    user = models.ForeignKey(TmsUser, on_delete="CASCADE", related_name="bucket")