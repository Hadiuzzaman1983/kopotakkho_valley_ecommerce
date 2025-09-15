from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount = models.PositiveIntegerField(help_text="discount in percent")
    active = models.DateTimeField()
    active_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code