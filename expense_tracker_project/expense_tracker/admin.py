from django.contrib import admin
from .models import Items, Expense, Income

admin.site.register(Items)
admin.site.register(Expense)
admin.site.register(Income)