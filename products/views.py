from django.shortcuts import render, get_object_or_404
from products.models import Category, Product, Comment

def products(request):
    ctx = {'products': Category.objects.all()}
    return render(request, 'products/products.html', ctx)

def products_list(request, category_url):
    ctx = {'category': get_object_or_404(Category, category_url=category_url) }
    return render(request, 'products/products_list.html', ctx)

def product_detail(request,category_url, product_url):
    get_object_or_404(Category, category_url=category_url)
    product = get_object_or_404(Product, product_url=product_url)
    comments = product.comments.filter(active=True)
    if request.method == "POST":
        username = request.user
        body = request.POST['body']
        new_comment = Comment(user=username,product=product, body=body)
        new_comment.save()
        message_good = "نظر شما با موفقیت ثبت شد بعد از برسی نمایش داده میشود!"
        ctx = {'product': product, 'comments': comments, 'message_good':message_good}
        return render(request, 'products/product_detail.html', ctx)
    ctx = {'product': product, 'comments': comments}
    return render(request, 'products/product_detail.html', ctx)