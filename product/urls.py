
from django.urls import path
from .views import (
    Home,
    ContactView,
    ProductDetails,
    CategoryDetails,
    PaymentMethodListView,
    ProductList,
    SearchProducts,

)
urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('contact/',ContactView.as_view(),name='contact' ),
    path('product-details/<str:slug>/', ProductDetails.as_view(), name='product-details'),
    path('category-details/<str:slug>/',CategoryDetails.as_view(),name='category-details'),
    path('product-list/',ProductList.as_view(),name='product-list'),
    path('search-products/',SearchProducts.as_view(),name='search-products'),
    path("payment-methods/", PaymentMethodListView.as_view(), name="payment_methods"),
]