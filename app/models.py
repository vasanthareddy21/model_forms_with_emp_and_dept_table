from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    dept_loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    # mgr=models.CharField(max_length=4)
    comm=models.IntegerField(null=True,blank=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
