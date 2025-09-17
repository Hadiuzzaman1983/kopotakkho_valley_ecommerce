from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(help_text="discount in percent")
    active = models.BooleanField(default=True)
    active_date = models.DateField()
    expire_date = models.DateField()
    discount_coupon_amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.code