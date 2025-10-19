import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense, Income

# Create your views here.

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