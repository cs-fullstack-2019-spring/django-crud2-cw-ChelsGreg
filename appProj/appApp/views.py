from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppForm
from .models import Application

# Create your views here.

# FUNCTION TO LIST APPLICANTS IN INDEX FROM MODEL OBJECTS
def index(request):
    everyApp= Application.objects.all()

    return render(request, 'appApp/index.html', {'everyApp': everyApp})

# TO CREATE NEW APPLICANT
def create(request):
    newApp = AppForm(request.POST or None)
    if newApp.is_valid():
        newApp.save()
        return redirect('index')

    return render(request, 'appApp/create.html', {'newApp': newApp})

# EDIT
def editThis(request, id):
    person = get_object_or_404(Application, pk=id)
    changeForm = AppForm(request.POST or None, instance=person)
    if changeForm.is_valid():
        changeForm.save()
        return redirect('index')

    return render(request, 'appApp/create.html', {'newApp': changeForm})

# DELETE
def deleteThis(request, id):
    person = get_object_or_404(Application, pk=id)
    if request.method == "POST":
        person.delete()
        return redirect('index')

    return render(request, 'appApp/delete.html', {'byebye': person})

