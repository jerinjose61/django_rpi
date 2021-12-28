from django.shortcuts import render, redirect
from app.forms import StudentForm
from app.models import Student


# Create your views here.

def home(request):
    students = Student.objects.all()

    return render(request, 'app/home.html', dict(students=students))


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save()

        return redirect("app:home")
    else:
        form = StudentForm()
        
        return render(request, 'app/add_student.html', dict(form=form))


def edit_student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        form.save()

        return redirect("app:home")
    else:
        form = StudentForm(instance=student)

        return render(request, 'app/edit_student.html', dict(form=form))


def delete_student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        student.delete()

        return redirect("app:home")
    else:
        return render(request, 'app/delete_student.html')