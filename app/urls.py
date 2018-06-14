from django.conf.urls import url

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
