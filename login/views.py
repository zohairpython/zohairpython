from django.shortcuts import render , HttpResponse 

# Create your views here.
def index (request):
    return HttpResponse ("Please inpute CREDENTIALS to login your account")

