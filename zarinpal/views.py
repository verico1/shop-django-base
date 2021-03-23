# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse, request
from django.shortcuts import redirect, get_object_or_404, render
from zeep import Client
from accounts.models import Profile
from products.models import Product
from pay.models import Order, OrderItem
import datetime

def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0

MERCHANT = 'fcb1583e-3ddc-11ea-8acf-000c295eb8fc'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
amount = ""
description = ""  # Required
email = "username.email"  # Optional
mobile = "sername.profile.phone_number" # Optional
CallbackURL = 'http://127.0.0.1:8000/payment/verify/' # Important: need to edit for realy server.

def send_request(request):
    username = request.user
    amount = get_user_pending_order(request).get_cart_total()
    email = username.email  # Optional
    mobile = username.profile.phone_number  # Optional
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    username = request.user
    email = username.email  # Optional
    mobile = username.profile.phone_number  # Optional
    amount = get_user_pending_order(request).get_cart_total()
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order_to_purchase = get_user_pending_order(request)
            order_to_purchase.is_ordered=True
            order_to_purchase.date_ordered=datetime.datetime.now()
            order_to_purchase.save()
            
            order_items = order_to_purchase.items.all()
            # a = order_items.product_status_number - 1
            # a.save()
            order_items.update(is_ordered=True, date_ordered=datetime.datetime.now())
            # user_profile = get_object_or_404(Profile, user=request.user)
            # user_profile.ebooks.add(*order_products)
            # user_profile.save()
            ctx = {'message_bad':'پرداخت با موفقیت انجام شد' + str(result.RefID)}
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        ctx = {'message_bad':'پرداخت با مشکل مواجه شده است یا توسط کاربر لغو شده'}
    return render(request, 'pay/verify.html', ctx)    