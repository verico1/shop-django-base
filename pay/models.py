from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile
from products.models import Product
from django_jalali.db import models as jmodels

class OrderItem(models.Model):
    product = models.OneToOneField(Product, null=True, on_delete=models.SET_NULL)
    is_ordered = models.BooleanField(default=False)
    date_added = jmodels.jDateField(auto_now=True)
    date_ordered = jmodels.jDateField(null=True)
    quantity = models.IntegerField(default=0, verbose_name='quantity')

    def __str__(self):
        return '{0} - {1}'.format(self.product.product_model, self.quantity)  

class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem, related_name='item')
    date_ordered = jmodels.jDateField(auto_now=True)
    created_on_time = models.TimeField(auto_now_add=True,null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.product_price*item.quantity for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)        

