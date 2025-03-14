from django.contrib import admin
from .models import User, Message
from django.utils import timezone

class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "reciever", "date")
    list_filter = ("sender", "date")
    list_per_page = 20
    actions = ()
    

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("sender", "date")
        return ("firstname", )
admin.site.register(Message)



class UserAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone_number")
    list_filter = ("firstname", "phone_number")
    
admin.site.register(User)



