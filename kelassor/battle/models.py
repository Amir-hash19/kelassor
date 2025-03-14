from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime


class User(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    phone_number = PhoneNumberField(region="IR", unique=True)

    def __str__(self):
        return F"{self.firstname} {self.lastname}"

class Message(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="sent_message")
    reciever = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="recieved_message", null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} {self.date}"

