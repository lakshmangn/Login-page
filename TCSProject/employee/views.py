from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_from(request,id=0):
    if request.method=='GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee=Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,'employee/employee_from.html',{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)

            
        if form.is_valid():
            form.save()

        return redirect('/employee/list')

def employee_list(request):
    context={'employee_list': Employee.objects.all()}
    return render(request,'employee/employee_list.html',context)


def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()

    return redirect('/employee/list')

