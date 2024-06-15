from django.db import models


class Inspector(models.Model):
    inspector = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.inspector
