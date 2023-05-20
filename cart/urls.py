from django.urls import path
from . import views

app_name = 'cart'
urpatterns = path(
    'add_to_cart/',
    views.CartItemCreateView.as_view(),
    name='add_to_cart'
)