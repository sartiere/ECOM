from django.urls import path
from . import views
from shop.views import index, detail, checkout,confirmation

urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', detail, name="detail"),
    path('checkout', checkout, name="checkout"),
    path('confirmation', confirmation, name="confirmation"),
    path('produits/', views.product_list, name='product_list'),  # Le '/' à la fin est important
    path('produits/<int:product_id>/', views.product_detail, name='product_detail'),
]
