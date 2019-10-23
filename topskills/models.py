from datetime import datetime

from django.db import models


class Job(models.Model):
    job_hash = models.CharField(max_length=255, unique=True)
    job_description = models.CharField(max_length=1000, default='')
    date_found = models.DateTimeField()
    date_viable_to = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.job_hash


class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    job_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.keyword
