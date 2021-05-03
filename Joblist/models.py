from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=150,null=True)
	jobtitle=models.CharField(max_length=100,null=True)
	jobdescription=models.CharField(max_length=1500,null=True)
	salary=models.IntegerField(null=True)
	experience=models.IntegerField(null=True)
	location=models.CharField(max_length=1500,null=True)
	startdate=models.DateField(null=True)
	enddate=models.DateField(null=True)

	def _str_(self):
		return self.name

class Candidates(models.Model):
	category=(('Male','male'), ('Female','female'),('Other','other'))
	name=models.CharField(max_length=150,null=True)
	dateofbirth=models.DateField(null=True)
	gender=models.CharField(max_length=150,null=True,choices=category)
	contactnumber=models.CharField(max_length=150,null=True)
	email=models.CharField(max_length=150,null=True)
	qualification=models.CharField(max_length=100,null=True)
	resume=models.FileField(null=True)
	company=models.CharField(max_length=200,null=True)
	def _str_(self):
		return self.name
