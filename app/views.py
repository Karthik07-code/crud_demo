from django.shortcuts import render, redirect
from app.forms import StudentForm
from .models import Student


def read_view(request):
    student_datas = Student.objects.all()
    return render(request, "index.html", {"table_datas": student_datas})


def create_view(request):
    # This below line creates an empty form [instance of the class Studentform()].
    form = StudentForm()
    if request.method == "POST":
        # This below line creates a form instance using the data the user submitted.
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "create.html", {"std_form": form})
"""
Final Analogy for def create_view():

    Line	                              Real-World Analogy
form = StudentForm()	            Giving a blank application form to a student
form = StudentForm(request.POST)	Taking the filled form back from the student
.is_valid()                     	Checking if the form was filled correctly
form.save()	                        Approving and saving it into the records
render(...)	                        Showing the form with entered details to the user again
"""
# flow chart : User Fills Form ➝ Submits ➝ Django Validates ➝ Saves to DB ➝ Redirect


def delete_view(request, id):
    student_datas = Student.objects.get(id=id)
    student_datas.delete()
    return redirect("/")


def update_view(request, id):
    student_datas = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student_datas)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = StudentForm(instance=student_datas)
    return render(request, "update.html", {"std_form": form})
