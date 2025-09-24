from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nick_name','first_name','last_name','avatar', 'about']

