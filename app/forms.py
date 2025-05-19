from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "regno": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your regno"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your name"}
            ),
            "dob": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Enter your dob"}
            ),
            "department": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your department"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your address"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your phone"}
            ),
        }
