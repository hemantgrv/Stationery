from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import Order,OrderItems

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request, 'shop/orders/orders.html', context)

def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItems.objects.filter(order=order)
    context = {'order':order, 'orderitems':orderitems}
    return render(request, 'shop/orders/view.html', context)
