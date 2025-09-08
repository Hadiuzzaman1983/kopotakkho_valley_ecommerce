from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100,unique=True)
    slug= models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['title']
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug= models.SlugField(unique=True,max_length=150)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    thumbnail = models.URLField()
    description = models.TextField(null=True, blank=True,default='N/A')
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title

    @property
    def related(self):
        return self.category.products.all().exclude(pk=self.pk)


class Slider(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(null=True, blank=True)
    show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title










class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)   # যেমনঃ "bKash", "Nagad", "Credit Card"
    description = models.TextField(blank=True, null=True)  # অতিরিক্ত তথ্য
    is_active = models.BooleanField(default=True)  # সক্রিয় আছে কি না

    def __str__(self):
        return self.name