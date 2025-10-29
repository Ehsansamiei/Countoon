#EHsan

#Imports
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Expense, Income
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)




def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
        return render(request, 'login.html')
    
    return render(request, 'login.html')


def logout_views(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    #Only bring the data of this user
    incomes = Income.objects.filter(user = request.user).order_by('-date')[:50]
    expenses = Expense.objects.filter(user= request.user).order_by('-date')[:50]
    total_income = sum(i.amount for i in incomes)
    total_expenses = sum(i.amount for i in expenses)

    context = {
        'incomes':incomes,
        'expenses':expenses,
        'total_income': total_income,
        'total_expense': total_expenses,
    }
    return render(request, 'dashboard.html', context)


@login_required
def add_record(request):
    if request.method == 'POST':
        record_type = request.POST.get('record_type')
        amount = request.POST.get('amount', '').replace(',', '')
        text = request.POST.get('text','')
        date = request.POST.get('date') or timezone.now()

        if record_type == 'income':
            Income.objects.create(user = request.user, amount = amount, text = text, date = date)
        elif record_type == 'expense':
            Expense.objects.create(user = request.user, amount = amount, text = text, date = date)
        return redirect('dashboard')
    return redirect('dashboard')


@login_required
def delete_record(request, record_type, pk):
    if record_type == 'income':
        record = get_object_or_404(Income, pk=pk, user=request.user)
    else:
        record = get_object_or_404(Expense, pk=pk, user=request.user)
    
    record.delete()
    return redirect('dashboard')


@login_required
def add_expense(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        text = request.POST.get('text')
        date = request.POST.get('date')
        Expense.objects.create(user = request.user, amount = amount, text = text, date = date)
        return redirect('dashboard')
    return render(request, 'add_expense.html')


@login_required
def add_income(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount'))
        text = request.POST.get('text')
        date = request.POST.get('date')
        Income.objects.create(user = request.user, amount = amount, text = text, date = date)
        return redirect('dashboard')
    return redirect(request, 'add_income.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("User created: ", user.username)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@csrf_exempt
def submit_income(request):
    """ user submits an income"""
    #TODO: validate data, user might be fake, token might be fake, amount might be fake and ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now = datetime.datetime.now() #TODO: user might want to submit the date herself 

    Income.objects.create(user = this_user, amount = request.POST['amount'],
            text = request.POST['text'], date = request.POST['date'])
    
    print(request.POST)
    print("method:", request.method)
    print("GET data:", request.GET)
    print("POST data:", request.POST)
    return JsonResponse({
        'status' : 'ok'
    })   



@csrf_exempt
def submit_expense(request):
    """ user submits an expense"""
    #TODO: validate data, user might be fake, token might be fake, amount might be fake and ...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now = datetime.datetime.now() #TODO: user might want to submit the date herself 

    Expense.objects.create(user = this_user, amount = request.POST['amount'],
            text = request.POST['text'], date = request.POST['date'])
    
    print(request.POST)
    print("method:", request.method)
    print("GET data:", request.GET)
    print("POST data:", request.POST)
    return JsonResponse({
        'status' : 'ok'
    })   

