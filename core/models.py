from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


def f(**kwargs):
    return kwargs


AUTHOR = 1
REVIEWER = 2

ROLE_CHOICES = (
    (AUTHOR, 'AUTHOR'),
    (REVIEWER, 'REVIEWER'),
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        superuser = self.model(email=self.normalize_email(email), **extra_fields)
        superuser.set_password(password)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=AUTHOR)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return 'User is - {}'.format(self.email)


