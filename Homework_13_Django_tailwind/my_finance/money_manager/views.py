from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'money_manager/index.html')


def statistics(request):
    return render(request, 'money_manager/statistics.html')
