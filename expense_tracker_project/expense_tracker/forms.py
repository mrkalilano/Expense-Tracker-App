from django import forms
from .models import Expense
from .models import Income

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['month', 'monthly_salary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['month'].widget.attrs['placeholder'] = 'Enter the month'
        self.fields['monthly_salary'].widget.attrs['placeholder'] = 'Enter the monthly salary'