from django.contrib import admin
from .models import User, Message
from django.utils import timezone

class MessageAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone_number")
    list_filter = ("firstname", "phone_number")
    list_per_page = 20
    

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("firstname", "lastname")
        return ("firstname", )
    


admin.site.register(Message)
admin.site.register(User)


