from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from accounts.models import Profile
from products.models import Product
from pay.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from pay.extras import generate_order_id
from django.contrib import messages
from django.db.models import F

def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id',"")).first()
    order_item, status = OrderItem.objects.get_or_create(product=product)
    order_item.quantity = order_item.quantity + 1
    order_item.save()
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        order_item.quantity = order_item.quantity + 1
        order_item.save()
        user_order.ref_code = generate_order_id()
        user_order.save()
    return redirect('/payment/order-summary/')

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {'order': existing_order}
    return render(request, 'pay/order_summary.html', context)   

@login_required()
def inc_from_cart(request, item_id):
    obj, status = OrderItem.objects.get_or_create(pk=item_id)
    obj.quantity = obj.quantity + 1
    obj.save()
    return redirect("/payment/order-summary/")

@login_required()
def red_from_cart(request, item_id):
    obj, status = OrderItem.objects.get_or_create(pk=item_id)
    obj.quantity = obj.quantity - 1
    obj.save()
    return redirect("/payment/order-summary/")    

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect("/payment/order-summary/")

@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    ctx = {'order':existing_order}
    return render(request, 'pay/checkout.html',ctx)
