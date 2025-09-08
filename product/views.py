from django.shortcuts import render
from django.views import generic
from .models import PaymentMethod, Category, Product, Slider


# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'featured_categories': Category.objects.filter(featured=True),
            'featured_products': Product.objects.filter(featured=True),
            'sliders': Slider.objects.filter(show=True),

        })
        return context

class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product/product-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context

class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'product/category-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_object().products.all()
        return context

class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




class PaymentMethodListView(generic.ListView):
    model = PaymentMethod
    template_name = "product/payment_methods.html"   # টেমপ্লেটের নাম
    context_object_name = "payment_methods"  # টেমপ্লেটে ব্যবহার করার নাম

    def get_queryset(self):
        # শুধু Active Payment Methods দেখাবে
        return PaymentMethod.objects.filter(is_active=True)

