from django.conf.urls import url
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.event_dis,name = 'event_dis'),
    url(r'^searchresults/',views.search_event, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^manage_event/$', views.manage_event, name='manage_event'),
    url(r'^update/(?P<event_id>\d+)/$', views.update_event, name='update_event'),
    url(r'^ajax/search/event/', views.search_event, name='search_event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
