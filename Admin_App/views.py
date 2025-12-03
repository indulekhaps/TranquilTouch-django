from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Categorydb, Servicedb,Staffdb
from django.http import JsonResponse


# Create your views here.
def dashboard(request):
    return render(request, "Dashboard.html")


def admin(request):
    return render(request, "Admin_Login.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('your_name')
        pwd = request.POST.get('your_pass')
        if User.objects.filter(username__contains=un).exists():
            data = authenticate(username=un, password=pwd)
        if data is not None:
            login(request, data)
            return redirect(dashboard)
        else:
            return redirect(admin)
    else:
        return redirect(admin)


def admin_services(request):
    cat = Categorydb.objects.all()
    return render(request, "Add_Services.html", {'cat': cat})


def save_services(request):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        category_id = request.POST.get('Category')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        description = request.POST.get('description')
        status = request.POST.get('status')
        image = request.FILES.get('service_image')
        obj = Servicedb(Service_Name=service_name, Category_id=category_id, Price=price, Duration=duration,
                        Description=description, Status=status, Service_Image=image)
        obj.save()
        return redirect(admin_services)

def view_services(request):
    data = Servicedb.objects.all()
    return render(request, "View_Services.html",{'data':data})

def edit_services(request, service_id):
    service = Servicedb.objects.get(id=service_id)
    categories = Categorydb.objects.filter(Status="Active")
    return render(request, "Edit_Services.html", {'Service': service, 'cat': categories})

def update_services(request,s_id):
    if request.method == "POST":
        service_name = request.POST.get('service_name')
        category_id = request.POST.get('Category')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        description = request.POST.get('description')
        status = request.POST.get('status')
        try:
            image = request.FILES['service_image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=Servicedb.objects.get(id=s_id).Service_Image
        Servicedb.objects.filter(id=s_id).update(Service_Name=service_name, Category_id=category_id, Price=price, Duration=duration,
                        Description=description, Status=status, Service_Image=file)
        return redirect(view_services)

def delete_services(request,service_id):
    data=Servicedb.objects.filter(id=service_id)
    data.delete()
    return redirect(view_services)

def category(request):
    return render(request, "Category.html")


def save_category(request):
    if request.method == "POST":
        c_name = request.POST.get('category_name')
        c_status = request.POST.get('status')
        c_description = request.POST.get('description')
        c_img = request.FILES['cat_image']
        obj = Categorydb(Category_Name=c_name, Status=c_status, Description=c_description, Category_Image=c_img)
        obj.save()
        return redirect(category)


def view_category(request):
    data = Categorydb.objects.all()
    return render(request, "View_Category.html", {'data': data})


def edit_category(request, category_id):
    category = Categorydb.objects.get(id=category_id)
    return render(request, "Edit_Category.html", {'category': category})


def update_category(request, c_id):
    if request.method == "POST":
        c_name = request.POST.get('category_name')
        c_status = request.POST.get('status')
        c_description = request.POST.get('description')
        try:
            c_img = request.FILES['cat_image']
            fs = FileSystemStorage()
            file = fs.save(c_img.name, c_img)
        except MultiValueDictKeyError:
            file = Categorydb.objects.get(id=c_id).Category_Image
        Categorydb.objects.filter(id=c_id).update(Category_Name=c_name, Status=c_status, Description=c_description,
                                                  Category_Image=file)
        return redirect(view_category)


def delete_category(request, category_id):
    data = Categorydb.objects.filter(id=category_id)
    data.delete()
    return redirect(view_category)

def add_staff(request):
    cat = Categorydb.objects.all()
    services = Servicedb.objects.all()
    return render(request,"Add_Staff.html", {'cat': cat, 'services': services})

def save_staff(request):
    if request.method == "POST":
        s_name=request.POST.get('staff_name')
        s_role=request.POST.get('role')
        s_category=request.POST.get('work_category')

        selected_services = request.POST.getlist('services')
        s_services = ",".join(selected_services)

        s_phone=request.POST.get('phone')
        s_email=request.POST.get('email')
        s_experience=request.POST.get('experience')
        s_salary=request.POST.get('salary')
        s_img=request.FILES['staff_image']
        obj=Staffdb(Staff_Name=s_name, Role=s_role, Work_category=s_category,Services=s_services,
                    Phone=s_phone,Email=s_email,Experience=s_experience,Salary =s_salary,Staff_image=s_img)
        obj.save()
        return redirect(add_staff)

def get_services_by_category(request):
    category_name = request.GET.get("category")

    if not category_name:
        return JsonResponse({"services": []})

    # Filter using the Category foreign key
    filtered_services = Servicedb.objects.filter(Category__Category_Name=category_name)

    data = {
        "services": [
            {"id": s.id, "name": s.Service_Name}
            for s in filtered_services
        ]
    }

    return JsonResponse(data)