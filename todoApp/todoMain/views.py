from django.shortcuts import render, HttpResponse
from .forms import RegisterForm

# Create your views here.
def home(request):
    return HttpResponse(request, "index.html")


def register_view(request):
    form = RegisterForm()
    context = {
        'form':form
    }
    return HttpResponse(request,"register.html", context)    

def login_view(request):
    return HttpResponse(request,"login.html")   

def logout_view(request):
    return HttpResponse("Logout")     

def  delete_task(request, id):
    return HttpResponse('Deleted')   