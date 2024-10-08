from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def courses_list(request):
    courses = Course.objects.all()
    return render(request,'courses.html', context={'courses': courses})


def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    course.views += 1
    course.save()
    return render(request,'course_details.html', context={'course': course})

def add_course(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        if title and description:
            Course.objects.create(title=title, description=description)
            return redirect('/course/list')
    return render(request, 'add_course.html')

