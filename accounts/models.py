from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    GENDER = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    gender = models.CharField(null=True, max_length=1, blank=True, choices=GENDER ,verbose_name="جنسیت")
    location = models.CharField(max_length=30, null=True, blank=True)
    profile_img = models.ImageField(upload_to='users', default='', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)    