from django.forms import ModelForm
from models import Income, Expense


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
