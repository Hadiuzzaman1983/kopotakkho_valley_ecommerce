from django.shortcuts import render
from django.views import generic
from .models import PaymentMethod
# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'
    
class ProductDetails(generic.TemplateView):
    template_name = 'product/product-details.html'





class PaymentMethodListView(generic.ListView):
    model = PaymentMethod
    template_name = "product/payment_methods.html"   # টেমপ্লেটের নাম
    context_object_name = "payment_methods"  # টেমপ্লেটে ব্যবহার করার নাম

    def get_queryset(self):
        # শুধু Active Payment Methods দেখাবে
        return PaymentMethod.objects.filter(is_active=True)

