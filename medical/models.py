from django.db import models

class Medicine(models.Model):
    key = models.CharField(primary_key=True, max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        app_label = 'medical'

    def __str__(self):
        return self.key
