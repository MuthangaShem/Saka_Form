from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
# <<<<<<< HEAD
#     url(r'signup/$', views.SignUp.as_view(), name='signup')
# ]
# =======
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
