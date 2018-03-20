# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import Course
# Create your views here.
def index(request):
    return render(request, "signup/index.html")

def courses(request):
    context = {
        "all_courses" : Course.objects.all(),
    }
    return render(request, "signup/index.html", context)


def add(request):
    validations = Course.objects.basic_validator(request.POST)
    if len(validations) == 0:
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc'],
        )
        return redirect('/courses')
    else:
        for error in validations:
            messages.add_message(request, messages.INFO, error)
        return redirect('/')

def destroy(request, id):
    context = {
        "course" : Course.objects.get(id=id)
        
    }
    
    
    return render (request, "signup/destroy.html", context)

def no(request):
    return redirect ('/courses')

def yes(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    return redirect ("/courses")

