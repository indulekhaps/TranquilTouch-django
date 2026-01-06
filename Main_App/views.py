from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Admin_App.models import Categorydb, Servicedb,Staffdb
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,"Index.html")

def about(request):
    return render(request, "About.html")

def services(request):
    return render(request, "Add_Services.html")

def work(request):
    return render(request, "Work.html")

def blog(request):
    return render(request, "Blog.html")

def contact(request):
    return render(request, "Contact.html")

def appointment(request):
    cat = Categorydb.objects.all()
    services = Servicedb.objects.all()
    return render(request,"Book_Appointment.html",{'cat': cat, 'services': services})

# def save_appointment(request):
