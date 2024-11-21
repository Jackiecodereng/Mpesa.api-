import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def trigger(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0798017611'
    amount = 1
    account_reference = '001-Barbie'
    transaction_desc = 'X-services'
    callback_url = 'https://termite-key-cow.ngrok-free.app'   #copy code from ngrok
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)



@csrf_exempt       # removes the csrf token
def callback(request):
    result = json.loads(request.body)
    print(result)
    return HttpResponse("ok")