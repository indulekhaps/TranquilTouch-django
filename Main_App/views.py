from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

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

