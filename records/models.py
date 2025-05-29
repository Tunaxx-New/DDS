from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model


class Purpose(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Record categories"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory')
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Record subcategories"


class Record(models.Model):
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    sum = models.DecimalField(max_digits=14, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.category}/{self.subcategory} - {self.sum}'

    class Meta:
        verbose_name_plural = "Record categories"
