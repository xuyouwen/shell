from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.template.loader import get_template
from models import Student

def all(request):
    students = Student.objects.all()
    return render_to_response('students.html', {'students': students})

def modify(request, sid):
    student = Student.objects.get(id=sid)
    return render_to_response('student.html', {'student': student})

def delete(request, sid):
    s = Student(id=sid)
    s.delete()
    return HttpResponseRedirect('/students/')

def add(request):
    return render_to_response('student.html')

def update(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        website = request.POST['website']
        sex = request.POST['sex']
        birth = request.POST['birth']
        address = request.POST['address']
        id = request.POST['id']
        s = Student(name=name,
                    email=email,
                    website=website,
                    sex=sex,
                    birth=birth,
                    address=address)
        if id != "":
            s.id = id
        s.save()
        return HttpResponseRedirect('/students/')