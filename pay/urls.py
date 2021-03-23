from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<slug:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('order-summary/', views.order_details, name="order-summary"),
    path('item/delete/<slug:item_id>/', views.delete_from_cart, name="delete_from_cart"),
    path('item/add/<slug:item_id>/', views.inc_from_cart, name="inc_from_cart"),
    path('item/red/<slug:item_id>/', views.red_from_cart, name="red_from_cart"),
    path('checkout/', views.checkout, name="checkout"),
]
