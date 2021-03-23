from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from products.models import Product, Category, Comment, Brand
from django.contrib.auth import authenticate, login, logout
from app.utils import grecaptcha_verify
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pay.views import get_user_pending_order
from pay.models import OrderItem, Order
from app.models import note, call_us


def staff_login(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('/staff/home/')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست ربات را کامل کنید'}
        elif user is not None:
            login(request, user)
            return redirect('/staff/home/')
        else:
            context = {'message_bad':'نام کاربری یا کلمه عبور اشتباه است'}
    else:
        context = {'message_bad':'ورود مجاز نیست'}            
    return render(request, "staff/staff_login.html", context)    
       
def staff_base(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        ctx = {'username':username}
        return render(request, 'staff/base.html',ctx)       
    else:
        return redirect('/staff')

def messages(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        messages = call_us.objects.all()
        ctx = {'username':username, 'messages':messages}
        return render(request, 'staff/messages.html',ctx)       
    else:
        return redirect('/staff')

def staff_home(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        users_count = User.objects.all().count()
        active_users_count = User.objects.filter(is_active=True).count()
        orders_count = Order.objects.filter(is_ordered=True).count()
        confirmed_orders_count = Order.objects.filter(is_ordered=False).count()
        ctx = {'username':username,
        'users_count':users_count,
        'confirmed_orders_count':confirmed_orders_count,
        'orders_count':orders_count,
        'active_users_count':active_users_count,
        }
        return render(request, 'staff/home.html',ctx)       
    else:
        return redirect('/staff')

def products_list(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        products = Product.objects.all()
        ctx = {'products':products, 'username':username}
        return render(request, 'staff/products_list.html',ctx)       
    else:
        return redirect('/staff')

class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    fields = ["brand_name",
    "brand_name_fa",
    "brand_url",
    ]
    template_name = "staff/brand_create_update.html"

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ["category_name",
    "category_name_fa",
    "category_url",
    ]
    template_name = "staff/category_create_update.html"

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["product_model",
    "product_status",
    "product_status_number",
    "product_url",
    "product_category",
    "product_brand",
    "product_img",
    "product_screen_size",
    "product_code",
    "product_price",
    ]
    template_name = "staff/product_create_update.html"

def product_edit(request, product_url):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        product = get_object_or_404(Product, product_url=product_url)
        ctx = {'username':username, 'product':product}
        return render(request, 'staff/new_product.html',ctx)       
    else:
        return redirect('/staff')       

def comments(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        comments = Comment.objects.order_by('active', '-created_on','-created_on_time')
        ctx = {'username':username, 'comments':comments}
        return render(request, 'staff/comments_list.html',ctx)       
    else:
        return redirect('/staff')

def users(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        users = User.objects.filter(is_superuser=False, is_staff=False)
        ctx = {'username':username, 'users':users}
        return render(request, 'staff/users_list.html',ctx)       
    else:
        return redirect('/staff')

def user_detail(request, user):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        user = get_object_or_404(User, username=user)
        ctx = {'username':username, 'user':user}
        return render(request, 'staff/user_detail.html',ctx)       
    else:
        return redirect('/staff')

def orders_list(request):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        orders = Order.objects.order_by('-is_ordered')
        ctx = {'username':username, 'orders':orders}
        return render(request, 'staff/orders_list.html',ctx)       
    else:
        return redirect('/staff')

def order_detail(request, ref_code):
    if request.user.is_authenticated and request.user.is_staff or request.user.is_superuser:
        username = request.user
        username = get_object_or_404(User, username=username)
        order = get_object_or_404(Order ,ref_code=ref_code)
        ctx = {'username':username, 'order':order}
        return render(request, 'staff/order_detail.html',ctx)       
    else:
        return redirect('/staff') 