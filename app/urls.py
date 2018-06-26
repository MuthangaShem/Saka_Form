from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^manage_event/$', views.manage_event, name='manage_event'),
    url(r'^update/(?P<event_id>\d+)/$', views.update_event, name='update_event'),
    url(r'^register/(?P<event_id>\d+)/$', views.register_event, name='register'),
    url(r'^interests/$', views.interests, name='interests'),
    url(r'^interests/ajax/handle/$', views.ajax_handle_user_categories, name='handle_category'),
    url(r'^ajax/calc/cost/$', views.ajax_calculate_ticket_cost, name='calc_cost'),
    url(r'^ajax/search/$', views.ajax_search_event, name='search_event'),
    url(r'^ajax/accordion/$', views.ajax_accordion_redirect, name='process_accordion'),
    url(r'^ajax/subscribe/$', views.ajax_subscribe_user, name='subscribe'),
    url(r'^callback/$', views.africas_callback, name='africastalking_cal'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
