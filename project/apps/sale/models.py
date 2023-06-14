from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    cell = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    class Meta:
        verbose_name = "seller"
        verbose_name_plural = "sellers"

    def __str__(self):
        return f"{self.user.username}"


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    item = models.ForeignKey("item.Item", on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date_sale = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-date_sale",)

    def clean(self):
        if self.quantity > self.item.quantity:
            raise ValidationError("La cantidad vendida no puede ser mayor que la cantidad disponible en el producto.")

    def save(self, *args, **kwargs):
        self.total_price = self.item.price * self.quantity
        super().save(*args, **kwargs)
