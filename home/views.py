from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the Home page of my new website HELLO ")