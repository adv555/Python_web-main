from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Income, Expense, Category


# Create your views here.

@login_required
def index(request):
    return render(request, 'money_manager/transactions.html')


@login_required
def statistics(request):
    income_transactions = Income.objects.all()
    print('INCOME TRANSACTIONS', income_transactions)
    return render(request, 'money_manager/statistics.html')


@login_required
def create_income_transaction(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        category = request.POST['category']
        created = request.POST['created']

        print('PRINT', amount, description, category, created)
        new_income = Income(amount=amount, description=description)
        print('NEW INCOME', new_income)

        new_income.save()

        # return redirect('transactions:statistics')
    return render(request, 'money_manager/transactions.html')


@login_required
def get_income_transactions(request):
    income_transactions = Income.objects.all()
    print('INCOME TRANSACTIONS', income_transactions)
    return render(request, 'money_manager/transactions.html', {'income_transactions': income_transactions})  # NOQA
