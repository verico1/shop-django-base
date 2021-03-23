from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('<slug:category_url>/', views.products_list, name='products_list'),
    path('<slug:category_url>/<slug:product_url>/', views.product_detail, name='product_detail')
]
