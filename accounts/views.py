from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .utils import grecaptcha_verify
import random
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse


def logout_view(request):
    logout(request)
    return redirect("/")
 
def login_view(request):
    if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return redirect('/account/')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست ربات را کامل کنید'}
        elif user is not None:
            login(request, user)
            return redirect('/account/')
        else:
            context = {'message_bad':'نام کاربری یا کلمه عبور اشتباه است'}
    else:
        context = {}            
    return render(request, "account/login.html", context)    
       
code = random.randint(100000, 999999)
def register_view(request):
    if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return redirect('/account/')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        global user
        user = User(email=email, username=username)
        user.set_password(password)
        if User.objects.filter(email=request.POST['email']).exists():
            context = {'message_bad':'این پست الکتونیکی قبلا استفاده شده است'}
        elif not password == password1:
            context = {'message_bad':'کلمه عبور با هم مطابقت ندارد'}
        elif User.objects.filter(username=request.POST['username']).exists():
            context = {'message_bad':'این نام کاربری قبلا استفاده شده است'}
        elif not grecaptcha_verify(request):
            context = {'message_bad':'لطفا تست ربات را کامل کنید.'}
        else:
            global code
            subject = 'تشکر بابت ثبت نام'
            message = " این به معنای یک دنیا است برای ما" + str(code)
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email])
            user.is_active = False
            user.save()
            login(request, user)
            return redirect('email_activation/')   
    else:
        context = {}
    return render(request, 'account/register.html', context)

def email_activation(request):
    if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return redirect('/account/')
    elif request.method == "POST":
        global code
        email_activation = request.POST['email_activation']
        if str(email_activation) == str(code):
            user.is_active = True
            user.save()
            return redirect('account')
        else:
            context = {'message_bad':'کد فعالسازی اشتباه است', 'p':email_activation, 's':code}
    else:
        context = {}
    return render(request, 'account/email_activation.html', context)

def account_view(request):
    if request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        ctx = {'username':username}
        return render(request, "account/account.html", ctx)
    else: 
        return redirect("/account/login")  

def account_edit(request):
    if not request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return redirect("/account/login") 
    if request.method == "POST":
        new_username = request.POST['username']
        new_email = request.POST['email']
        new_first_name = request.POST['first_name']
        new_last_name = request.POST['last_name']
        new_phone_number = request.POST['phone_number']
        new_location = request.POST['location']
        new_gender = request.POST['gender']
        if not new_first_name == request.user.profile.first_name:
            username = request.user
            user_edit = get_object_or_404(User, username=username)
            user_edit.profile.first_name = new_first_name
            user_edit.profile.save()
            ctx = {'message_good':'ویرایش با موفقیت انجام شد'}
        if not new_last_name == request.user.profile.last_name:
            username = request.user
            user_edit = get_object_or_404(User, username=username)
            user_edit.profile.last_name = new_last_name
            user_edit.profile.save()
            ctx = {'message_good':'ویرایش با موفقیت انجام شد'}
        if not new_gender == request.user.profile.gender:
            username = request.user
            user_edit = get_object_or_404(User, username=username)
            user_edit.profile.gender = new_gender
            user_edit.profile.save()
            ctx = {'message_good':'ویرایش با موفقیت انجام شد'} 
        if not new_location == request.user.profile.location:
            username = request.user
            user_edit = get_object_or_404(User, username=username)
            user_edit.profile.location = new_location
            user_edit.profile.save()
            ctx = {'message_good':'ویرایش با موفقیت انجام شد'}
        if not new_phone_number == request.user.profile.phone_number:
            username = request.user
            user_edit = get_object_or_404(User, username=username)
            user_edit.profile.phone_number = str(new_phone_number)
            user_edit.profile.save()
            ctx = {'message_good':'ویرایش با موفقیت انجام شد'}
        if not new_email == request.user.email:
            if User.objects.filter(email=new_email).exists():
                ctx = {'message_bad':'این ایمیل قبلا استفاده شده است'}
            else:
                username = request.user
                user_edit = get_object_or_404(User, username=username)
                user_edit.email = new_email
                global code
                subject = 'تغییر ایمیل'
                message = " برای تایید تغییر ایمیل لطفا کد را وارد کنید" + str(code)
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject, message, email_from, [new_email])
                user_edit.save()
                return redirect('/account/sec_email_activation/')
        if not new_username == request.user.username:
            if User.objects.filter(username=new_username).exists():
                ctx = {'message_bad':'این نام کاربری قبلا استفاده شده است'}
            else:
                username = request.user
                user_edit = get_object_or_404(User, username=username)
                user_edit.username = new_username
                user_edit.save()
                ctx = {'message_good':'ویرایش با موفقیت انجام شد'}
        else:
            ctx = {}
    else:
        username = request.user
        user = get_object_or_404(User, username=username)
        ctx = {'user':user}
    return render(request, "account/account_edit.html", ctx)                 


def sec_email_activation(request):   
    if request.method == "POST":
        global code
        email_activation = request.POST['email_activation']
        username = request.user
        user_edit = get_object_or_404(User, username=username)
        if str(email_activation) == str(code):
            user_edit.is_active = True
            user_edit.save()
            login(request, user_edit)
            return redirect('/account/')
        context = {'message_bad':'کد فعالسازی اشتباه است', 'p':email_activation, 's':code}    
    else:
        context = {}
    return render(request, 'account/email_activation.html', context)


def password_works(request):
    if not request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return redirect("/account/login")
    else:
        if request.method == "POST":
            password = request.POST['password']
            new_password = request.POST['new_password']
            new_password_valid = request.POST['new_password_valid']
            user = User.objects.get(username=request.user)
            success = user.check_password(password)
            if not new_password == new_password_valid:
                ctx = {'message_bad':'رمز جدید با یکدیگر مطابقت ندارند'}   
            elif success:
                user.set_password(new_password)
                user.save()
                ctx = {'message_good':'رمز با موفقیت تغییر کرد'} 
            else:
                ctx = {'message_bad':'رمز فعلی شما اشتباه است'}
        else:
            ctx = {}         
        return render(request, "account/password_works.html", ctx)
 
def reset_password(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "بازیابی کلمه عبور"
                    email_template_name = "account/forget/password_reset_email.html"
                    full_name = user.profile.first_name +" "+ user.profile.last_name
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'فروشگاه',
                        'en_site_name': 'shop',
                        'full_name' : full_name,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/account/password_reset/done/")
            else:
                return redirect("/account/password_reset/done/")
    password_reset_form = PasswordResetForm()
    ctx={"password_reset_form": password_reset_form}
    return render(request, "account/forget/reset_password.html",ctx)    

   