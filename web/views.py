from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def submit_expense(request):
    """ user submits an expense"""
    print(request.POST)

    return JsonResponse({
        'status' : 'ok'
    })