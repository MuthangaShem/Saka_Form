from django.conf.urls import url
<<<<<<< HEAD
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
<<<<<<< HEAD
# <<<<<<< HEAD
#     url(r'signup/$', views.SignUp.as_view(), name='signup')
# ]
# =======
=======
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]
<<<<<<< HEAD
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
=======
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
