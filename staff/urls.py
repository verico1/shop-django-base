from django.urls import path
from staff import views

app_name="staff"

urlpatterns = [
    path('home/', views.staff_home, name='staff_home'),
    path('', views.staff_login, name='staff_login'),
    path('products_list/', views.products_list, name='products_list'),
    path('product_edit/<slug:product_url>/', views.product_edit, name='product_edit'),
    path('product_create/', views.ProductCreate.as_view(), name='product_create'),
    path('category_create/', views.CategoryCreate.as_view(), name='category_create'),
    path('brand_create/', views.BrandCreate.as_view(), name='brand_create'),
    path('comments/', views.comments, name='comments'),
    path('users/', views.users, name='users'),
    path('users/<slug:user>/', views.user_detail, name='user_detail'),
    path('orders_list/', views.orders_list, name='orders_list'),
    path('order_detail/<slug:ref_code>/', views.order_detail, name='order_detail'),
    path('messages/', views.messages, name='messages'),
]
