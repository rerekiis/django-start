from django.shortcuts import render, redirect
from django.http import request
from .forms import PersonForm
from .models import Person
# Create your views here.

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("person_list")
        

    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons':persons})
