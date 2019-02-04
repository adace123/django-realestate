from django.urls import path
from .views import CreateContactView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(CreateContactView.as_view()))
]
