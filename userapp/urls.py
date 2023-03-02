from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('login',views.login),
    path('showflower/<id>',views.showflower),
    path('viewdetails/<id>',views.viewdetails),
    path('signup',views.signup),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('MakePayment',views.MakePayment),
    path('removeItem',views.removeItem),
    path('addToCart',views.addToCart),
    path('signout',views.signout),
    path('search',views.search),
]
