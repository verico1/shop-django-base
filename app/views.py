from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import call_us, note
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from app.utils import grecaptcha_verify
from products.models import Product, Category
from django.db.models import Q

def index(request):
    ctx = {'note':note.objects.filter(active=True)}
    return render(request, 'index.html',ctx)

def not_found(request, exceptions):
    return render(request, 'error/404.html')

def server_error(request):
    return render(request, 'error/500.html')

def permission_denied(request, exceptions):
    return render(request, 'error/403.html')

def bad_request(request, exceptions):
    return render(request, 'error/400.html')

def search_view(request):
    query = request.GET.get('search')
    products = Product.objects.filter(
        Q(product_model__icontains=query)
    )
    ctx = {'products':products}
    return render(request,"search.html", ctx)

def call_us_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        call = call_us(name=name, email=email, content=content)
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست ربات را کامل کنید'}
        else:    
            call.save()
            subject = 'پیام شما با موفقیت ارسال شد'
            message = " پیام شما با موفقیت ارسال شد"
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email])
            context = {'message_good':'پیام شما با موفقیت ارسال شد'}
    elif request.user.is_authenticated:
        eamil = request.user.email
        context = {'email':eamil}       
    else:
        context = {}
        
    return render(request, "call_us.html", context)    
