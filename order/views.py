from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# Create your views here.

class Checkout(generic.View):
    login_url = reverse_lazy('login')
    def get(self, *args, **kwargs):
        form=CheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request,'order/checkout.html',context)


