from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin

<<<<<<< HEAD
# Create your models here.


class User(User, PermissionsMixin):
    def __str__(self):
# <<<<<<< HEAD
#         return f"@{username}"
# =======
        return f"@{username}"
# >>>>>>> 5621387e0888a58f5dc24579ce31704187eb6729
=======

class User(User, PermissionsMixin):
    def __str__(self):
        return f"@{username}"
>>>>>>> 0dc7e00b9902c6ec5425bace5c6e33b3e64bd9de
