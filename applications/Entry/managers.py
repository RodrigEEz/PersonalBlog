from django.db import models

class EntryManager(models.Manager):

    def entry_in_cover(self):
        return self.filter(
            public = True,
            cover_page = True
        ).order_by('-created').first()

    def entry_in_home(self):
        return self.filter(
            public = True,
            in_home = True
            ).order_by('-created')[:4]

    def recent_entries(self):
        return self.filter(
            public = True
            ).order_by('-created')[:6]