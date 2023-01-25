
from django.urls import path
from .views import *


app_name = "cart"
urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add_to_cart/<slug>', cart, name='add_to_cart'),
    path('remove_cart/<slug>', removecart, name='remove_cart'),
    path('delete_cart/<slug>', deletecart, name='delete_cart'),
    

]