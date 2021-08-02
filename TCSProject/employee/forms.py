from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'mobile':'Phone Number',
            'emp_code':'Employee No',
            'fullname':'Full Name'
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['emp_code'].required= False
        self.fields['position'].empty_label= "Select Any Postion"


