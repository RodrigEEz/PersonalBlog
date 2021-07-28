from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from ..User.models import User
from ..Entry.models import Entry

class Favorite(TimeStampedModel):

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        db_table = "favorite"
        unique_together = ["User", "Entry"]

    def __str__(self):
        return self.Entry.title
