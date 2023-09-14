from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_dept(request):
    EDFO=DeptForm()
    d={'EDFO':EDFO}
    if(request.method=='POST'):
        DFO=DeptForm(request.POST)
        if(DFO.is_valid()):
            DFO.save()
            return HttpResponse('dept table data is insertd')
    return render(request,'insert_dept.html',d)

def insert_emp(request):
    EEFO=EmpForm()
    d={'EEFO':EEFO}
    if(request.method=='POST'):
        DEFO=EmpForm(request.POST)
        if(DEFO.is_valid()):
            DEFO.save()
            return HttpResponse('emp table data is insertd')
    return render(request,'insert_emp.html',d)
