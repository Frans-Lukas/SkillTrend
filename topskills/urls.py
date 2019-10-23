from django.urls import path
from . import views


app_name = 'topskills'
urlpatterns = [
    path('', views.index, name='index'),
    path('jobs-with-word/<slug:word>', views.jobs, name='jobs')
]