from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels


class call_us(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=128)
    content = models.TextField(max_length=1000)
    created_on = jmodels.jDateField(auto_now_add=True,null=True)

    def __str__(self):
        return " by %s ---- %s در تاریخ" % (self.name,self.created_on)

class note(models.Model):
    content = models.TextField(max_length=400)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.content