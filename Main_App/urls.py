from django.urls import path
from Main_App import views

urlpatterns=[
    path('Index/',views.index,name="index"),
    path('About/',views.about,name="about"),
    path('Services/',views.services,name="services"),
    path('Work/',views.work,name="work"),
    path('Blog/',views.blog,name="blog"),
    path('Contact/',views.contact,name="contact"),

]