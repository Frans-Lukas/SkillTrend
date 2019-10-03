from django.contrib import admin
from .models import Question
from topskills.models import Job, Keyword

admin.site.register(Question)
admin.site.register(Job)
admin.site.register(Keyword)
# Register your models here.
