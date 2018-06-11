from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    url(r'^create_event/$', views.create_event, name='create_event'),
]