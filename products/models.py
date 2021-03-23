from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.contrib.auth.models import User
from accounts.models import Profile
from django_jalali.db import models as jmodels

class Category(models.Model):
    category_name = models.CharField(max_length=60, default='', verbose_name="نام دسته")
    category_name_fa = models.CharField(max_length=60, default='', verbose_name="نام فارسی دسته")
    category_url = models.SlugField(max_length=200, default='', verbose_name="اسلاگ دسته")
    def __str__(self):
        return "%s" % (self.category_name)

    def get_absolute_url(self):
        return reverse("staff:products_list")
    

class Brand(models.Model):
    brand_name = models.CharField(max_length=60, default='', verbose_name="نام برند")
    brand_name_fa = models.CharField(max_length=60, default='', verbose_name="نام فارسی برند")
    brand_url = models.SlugField(max_length=200, default='', verbose_name="اسلاگ برند")
    def __str__(self):
        return "%s" % (self.brand_name)

    def get_absolute_url(self):
        return reverse("staff:products_list")
    

class Product(models.Model):
    STATUS = (
        (' ', 'موجود'),
        ('un', 'ناموجود'),
    )
    product_model = models.CharField(max_length=255, default='', verbose_name="نام محصول")
    product_status = models.CharField(null=True ,max_length=2 , choices=STATUS ,verbose_name="وضعیت موجودی")
    product_status_number = models.IntegerField(default=0, verbose_name="موجودی انبار")
    product_url = models.SlugField(max_length=200, default='', verbose_name="اسلاگ محصول" )
    product_category = models.ForeignKey(Category,
        verbose_name="دسته محصول",
        on_delete=models.CASCADE,
        default='',
        null=True,
        related_name="products",
    )
    product_brand = models.ForeignKey(Brand,
        on_delete=models.CASCADE,
        default='',
        null=True,
        related_name="products",
        verbose_name="برند محصول"
    )
    product_img = models.ImageField(upload_to="mobile",default='', verbose_name="تصویر محصول")
    product_screen_size = models.CharField(max_length=4,
        default='',
        verbose_name="اندازه صفحه نمایش"
    )
    product_code = models.CharField(max_length=6,
        default='',
        verbose_name="کد محصول"
    )     
    product_price = models.FloatField(null=True, verbose_name="قیمت محصول")

    def __str__(self):
        return "%s - %s: %s : %savailable" % (self.product_category, self.product_brand, self.product_model, self.product_status)

    def get_absolute_url(self):
        return reverse("staff:products_list")

class Comment(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User ,on_delete=models.CASCADE, max_length=80, related_name='comments_user')
    body = models.TextField()
    created_on = jmodels.jDateField(auto_now_add=True)
    created_on_time = models.TimeField(auto_now_add=True,null=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
