
from django.urls import path, include
from .views import (
    Home,
    ProductDetails,
    PaymentMethodListView,

)
urlpatterns = [
    path('',Home.as_view(),name='home' ),
    path('product-details/', ProductDetails.as_view(), name='product-details'),
    path("payment-methods/", PaymentMethodListView.as_view(), name="payment_methods"),
]