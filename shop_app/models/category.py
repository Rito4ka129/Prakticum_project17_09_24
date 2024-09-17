from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Categories'


class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    article = models.CharField(max_length=100, help_text='article',unique=True,db_index=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'quantity']