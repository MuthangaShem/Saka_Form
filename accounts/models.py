from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.


class User(User, PermissionsMixin):
    def __str__(self):
# <<<<<<< HEAD
#         return f"@{username}"
# =======
        return f"@{username}"
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
