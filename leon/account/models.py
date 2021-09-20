from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
    group=(
        ('AB+','AB'),
        ('A+','A+'),
        ('B+','B+'),
        ('O+','O+'),
        ('AB-','AB'),
        ('A-','A-'),
        ('B-','B-'),
        ('O-','O-'),
    )
    states=(
        ('Andra Pradesh','Andra Pradesh'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chhattisgarh','Chhattisgarh'),
        ('Goa','Goa'),
        ('Gujarat','Gujarat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Jammu Kashmir','Jammu Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('West Bengal','West Bengal'),
        ('Karnataka','Karnataka'),
        ('Kerala','Kerala'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Orissa','Orissa'),
        ('Punjab','Punjab'),
        ('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Tripura','Tripura'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Uttarakhand','Uttarakhand'),
        ('Thelughana','Thelughana'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    empid=models.CharField(max_length=108,null=True,blank=True)
    mobile=models.CharField(max_length=12,null=True,blank=True)
    email=models.EmailField(max_length=250,null=True,blank=True)
    sex=models.CharField(max_length=10,null=True,blank=True,choices=(('male','male'),('female','female')))
    dob=models.DateField(null=True,blank=True)
    doj=models.DateField(null=True,blank=True)
    blood_group=models.CharField(max_length=50,null=True,blank=True,choices=group)
    house=models.CharField(max_length=200,null=True,blank=True)
    street=models.CharField(max_length=200,null=True,blank=True)
    city=models.CharField(max_length=200,null=True,blank=True)
    state=models.CharField(max_length=200,null=True,blank=True,choices=states)
    pincode=models.CharField(max_length=200,null=True,blank=True)
    staff_type=models.CharField(max_length=200,null=True,choices=(('Operations','Operations'),('Sales','Sales'),('Trainer','Trainer'),('Admin','Admin')))   
    status=models.CharField(max_length=200,null=True,choices=(('Active','Active'),('Deactive','Deactive')))
    profile_pic=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
        
    