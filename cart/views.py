from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.views import generic
from .models import Coupon


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

    def get(self,request,*args,**kwargs):
        product_id = request.GET.get('product_id',None)
        quantity = request.GET.get('quantity',None)
        clear= request.GET.get('clear',False)
        cart = Cart(request)

        if product_id and quantity:
            product = get_object_or_404(Product, id=product_id)
            if int(quantity) > 0:
                if product.in_stock:
                    cart.update(int(product_id), int(quantity))
                    return redirect('cart')
                else:
                    messages.warning(request,'Product is not in stock')
                    return redirect('cart')
            else:
                cart.update(int(product_id), int(quantity))
                return redirect('cart')



        if clear:
            cart.clear()
            return redirect('cart')

        return super().get(request,*args,**kwargs)


class AddCoupon(generic.View):
    def post(self,request,*args,**kwargs):
        code= request.POST.get('coupon','')
        coupon = Coupon.objects.filter(code__iexact=code)
        cart = Cart(self.request)

        if coupon.exists():
            coupon = coupon.first()
            current_date = timezone.now()
            active_date =coupon.active_date
            expiry_date = coupon.expiry_date

            if current_date > expiry_date:
                messages.warning(request,'You cannot add a coupon that is expired')
                return redirect('cart')

            if current_date < active_date:
                messages.warning(request,'coupon is yet that is active')
                return redirect('cart')

            cart.add_coupon(coupon.id)
            messages.warning(request, 'Your coupon has been added successfully')
            return redirect('cart')

        else:
            messages.warning(request,'Invalid Coupon code')
            return redirect('cart')




