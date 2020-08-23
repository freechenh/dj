import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse('two index')


def add_student(request):
    student = Student()
    student.s_name = 'jerry%s' % random.randrange(0, 100)
    student.s_age = random.randrange(0, 100)
    student.save()
    return HttpResponse('add success')


def get_students(request):
    students = Student.objects.all()
    # for student in students:
    #     print(student.s_name)
    content = {
        "hobby": "play game",
        'students': students
    }
    return render(request, 'student_list.html', content)


def update_student(request):
    student = Student.objects.get(pk=9)
    student.s_name = 'jack'
    student.s_age = 200
    student.save()
    return HttpResponse('update success')


def delete_student(request):
    student = Student.objects.get(pk=10)
    student.delete()
    return HttpResponse('delete success')
