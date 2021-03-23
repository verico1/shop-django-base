# Generated by Django 3.1.5 on 2021-03-21 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(default='', max_length=60, verbose_name='نام برند'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name_fa',
            field=models.CharField(default='', max_length=60, verbose_name='نام فارسی برند'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_url',
            field=models.SlugField(default='', max_length=200, verbose_name='اسلاگ برند'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=60, verbose_name='نام دسته'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name_fa',
            field=models.CharField(default='', max_length=60, verbose_name='نام فارسی دسته'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_url',
            field=models.SlugField(default='', max_length=200, verbose_name='اسلاگ دسته'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_brand',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.brand', verbose_name='برند محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category', verbose_name='دسته محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(default='', max_length=6, verbose_name='کد محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='', upload_to='mobile', verbose_name='تصویر محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_model',
            field=models.CharField(default='', max_length=255, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(null=True, verbose_name='قیمت محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_screen_size',
            field=models.CharField(default='', max_length=4, verbose_name='اندازه صفحه نمایش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[(' ', 'موجود'), ('un', 'ناموجود')], max_length=2, null=True, verbose_name='وضعیت موجودی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.SlugField(default='', max_length=200, verbose_name='اسلاگ محصول'),
        ),
    ]