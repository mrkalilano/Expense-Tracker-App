from django.urls import path
from .views import home, expense_list, add_expense
from .views import home, expense_list, add_expense, sign_out, confirm_sign_out, income

app_name = 'expense_tracker'  # Add this line to define the app namespace

urlpatterns = [
    path('', home, name='home'),
    path('add_expense/', add_expense, name ='add_expense'),
    path('expense_list/', expense_list, name='expense_list'),
    path('sign_out/', sign_out, name='sign_out'),
    path('confirm_sign_out/', confirm_sign_out, name ='confirm_sign_out'),
    path('income/', income, name ='income'),  # Add this line for the income view
]