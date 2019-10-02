from django.db import models


class Job(models.Model):
    job_hash = models.CharField(max_length=255)
    date_found = models.DateTimeField()

    def __str__(self):
        return self.job_hash


class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    job_hash = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword
