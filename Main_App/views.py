from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Admin_App.models import Categorydb, Servicedb,Staffdb
from Main_App.models import Appointmentdb
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

def save_appointment(request):
    if request.method == "POST":
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        service = request.POST.get('service')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        staff_level = request.POST.get('staff_level')
        obj = Appointmentdb(
            Customer_name=customer_name,
            Phone=phone,
            Category=category,
            Service=service,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            staff_level=staff_level)
        obj.save()
        return redirect('appointment_success')

def appointment_success(request):
    return render(request, "Appointment_Success.html")