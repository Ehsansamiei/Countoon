from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def submit_expense(request):
    """ user submits an expense"""
    print(request.POST)
    print("method:", request.method)
    print("GET data:", request.GET)
    print("POST data:", request.POST)
    return JsonResponse({
        'status' : 'ok'
    })  