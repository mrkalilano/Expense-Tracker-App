# expense_tracker/models.py
from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.db.models import DecimalField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Items(BaseModel):
    # Define your expense model fields here
    Item = models.CharField(max_length=255)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Date = models.DateField()

    def __str__(self):
        return self.description

class Expense(BaseModel):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class add_expense(BaseModel):
    # Define your expense model fields here
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.description

class Income(models.Model):
    month = models.CharField(max_length=255)  # You can adjust the max length as needed
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Income for {self.month}"