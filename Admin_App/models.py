from django.db import models
STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
)

# Create your models here.
class Categorydb(models.Model):
    Category_Name= models.CharField(max_length=50,null=True,blank=True)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    Description=models.TextField(blank=True,null=True)
    Category_Image=models.ImageField(upload_to="Category",null=True,blank=True)

class Servicedb(models.Model):
    Service_Name =models.CharField(max_length=15,blank=True,null=True)
    Category = models.ForeignKey('Categorydb', on_delete=models.SET_NULL, null=True, blank=True)
    Price =models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    Duration=models.IntegerField(blank=True,null=True)
    Description=models.TextField(null=True, blank=True)
    Status= models.CharField(max_length=10,null=True,blank=True)
    Service_Image=models.ImageField(upload_to="Service", null=True, blank=True)

class Staffdb(models.Model):
    Staff_Name =models.CharField(max_length=15,blank=True,null=True)
    Role = models.CharField(max_length=50, null=True, blank=True)
    Work_category = models.CharField(max_length=50, null=True, blank=True)
    Services = models.TextField(null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Experience =models.CharField(max_length=50, null=True, blank=True)
    Salary = models.IntegerField(null=True, blank=True)
    Staff_image = models.ImageField(upload_to="Staff", null=True, blank=True)

