from django.urls import path
from .views import register_user, add_messgae, show_messages


urlpatterns = [
    path("signup-page",register_user),
    path("add-message", add_messgae),
    path("list-text", show_messages),

]