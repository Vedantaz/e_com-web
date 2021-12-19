
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="ShopHome"),
    
    path('about/', views.about,name="About"),

    path('contact/', views.contact,name="Contact"),
    
    path('products/', views.products,name="Product-list "),
    
    path('tracker/', views.tracker,name="Tracker"),
    
    path('search/', views.search,name="Search"),
    
    path('prodView/<int:myid>', views.prodView,name="Productview"),
    
    path('checkout/', views.checkout,name="Checkout"),
    
    path('trending/', views.checkout,name="Checkout"),
    
    path('discount/', views.checkout,name="Discount"),

]
