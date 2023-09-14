from django import forms
from app.models import *

class DeptForm(forms.ModelForm):
    class Meta:
        model=Dept
        fields='__all__'

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'
        