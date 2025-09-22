
from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkout'),

]