from django.urls import path
from Main_App import views

urlpatterns=[
    path('Index/',views.index,name="index"),
    path('About/',views.about,name="about"),
    path('Services/',views.services,name="services"),
    path('Work/',views.work,name="work"),
    path('Blog/',views.blog,name="blog"),
    path('Contact/',views.contact,name="contact"),
    path('Book_Appointments/',views.appointment,name="appointment"),
    path('Save_Appointment/',views.save_appointment,name="save_appointment"),
    path('Success_Appointment/',views.appointment_success,name="appointment_success"),

]