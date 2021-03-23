from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.account_view, name='account'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/email_activation/', views.email_activation, name='email_activation'),
    path('sec_email_activation/', views.sec_email_activation, name='sec_email_activation'),
    path('logout/', views.logout_view, name='logout_view'),
    path('edit/', views.account_edit, name='edit'),
    path('change_password/', views.password_works, name='password_works'),
    path('reset_password/', views.reset_password, name ='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = "account/forget/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "account/forget/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = "account/forget/password_reset_done.html"), name ='password_reset_complete')
]
