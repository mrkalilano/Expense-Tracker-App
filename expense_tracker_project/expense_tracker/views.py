from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.shortcuts import render
from django.contrib.auth import logout


def expense_list(request):
    # Fetch all expenses (you may filter based on user if needed)
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # Create Expense object but don't save it yet
            new_expense = form.save(commit=False)

            # Save the expense to the database
            new_expense.save()

            # Redirect to the expense list page
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    # Retrieve all expenses from the database
    expense_list = Expense.objects.all()

    return render(request, 'add_expense.html', {'form': form, 'expense_list': expense_list})
def home(request):
    return render(request, 'home.html')

def home_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()

    return render(request, 'home.html', {'form': form, 'expenses': expenses})

def sign_out(request):
    return render(request, 'sign_out.html')

def confirm_sign_out(request):
    if request.method == 'POST':
        # If the user confirms sign-out, log them out
        logout(request)
        return redirect('login')  # Redirect to the login page
    return redirect('home')  # If the user cancels, redirect them back to the home page
