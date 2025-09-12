from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .cart import Cart
from product.models import Product
# Create your views here.

class AddToCart(generic.View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)

        return redirect('cart')

class CartItem(generic.TemplateView):
    template_name = 'cart/cart.html'



