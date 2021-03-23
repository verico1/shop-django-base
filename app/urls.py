from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('call_us/', views.call_us_view, name="call_us"),
    path('search/', views.search_view, name="search_view"),
]
