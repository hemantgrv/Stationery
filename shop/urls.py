from django.urls import path 
from . import views
from shop import order 

urlpatterns = [
    path('',views.home, name="home"),
    path('register',views.register, name="register"),
    path('login',views.login_page, name="login"),
    path('logout',views.logout_page, name="logout"),
    path('cart',views.cart_page, name="cart"),
    path('fav',views.fav_page, name="fav"),
    path('favviewpage',views.favviewpage, name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav, name="remove_fav"),
    path('checkout',views.checkout, name="checkout"),
    path('remove_cart/<str:cid>',views.remove_cart, name="remove_cart"),
    path('collections',views.collections, name="collections"),
    path('collections/<str:name>',views.collectionsview, name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart, name="addtocart"),
    path('place-order',views.placeorder, name="placeorder"),   
    path('payment',views.payment, name="payment"),
    path('contact_form',views.contact_form, name="contact_form"),
    path('myorders',order.index, name="myorders"),
    path('view-order/<str:t_no>',order.vieworder, name="orderview"),
    path('report',views.show_products, name="showproduct"),
    path('report-2',views.show_items, name="showitems"),
]