from django import forms
from sqlcrud.models import Employee

class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        print(inputsal)
        if inputsal < 5000 :
            raise forms.ValidationError('The Minimum salary should be atleast 5k')
        return inputsal
    class Meta:
        model = Employee
        fields = '__all__'