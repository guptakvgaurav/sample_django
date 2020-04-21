from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


# Create your models here.
class Author(models.Model):
    PYTHON = 'PY'
    JAVA = 'JV'
    SWIFT = 'SW'
    JAVASCRIPT = 'JS'

    PROGRAMMING_LANGUAGES = [
        (PYTHON, 'Python'),
        (JAVA, 'Java'),
        (SWIFT, 'Swift'),
        (JAVASCRIPT, 'JavaScript'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        verbose_name=_('user'),
        on_delete=models.CASCADE
    )

    # first_name = models.TextField(max_length=255)
    # last_name = models.TextField(max_length=255)
    age = models.IntegerField(blank=True, default=-1)
    designation = models.TextField(blank=True, default='')
    skills = models.CharField(
        max_length=2,
        choices=PROGRAMMING_LANGUAGES,
        default=PYTHON,
    )

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        author_profile = Author(user=instance)
        print('########## Author profile - {}'.format(author_profile))
        author_profile.save()
