from django.shortcuts import render
from django.http.response import HttpResponse
from battle.models import User, Message
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_user = User.objects.create(
            firstname = data.get("firstname"),
            lastname = data.get("lastname"),
            phone_number = data.get("phone_number"),            
        )
        return HttpResponse(f"{created_user.id}user created succesfully")
    

@csrf_exempt
def add_messgae(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Message.objects.create(
            sender_id = data.get("sender"),
            reciever = None,
            text = data.get("text"),
        )
        return HttpResponse("text created succesfully")




        



