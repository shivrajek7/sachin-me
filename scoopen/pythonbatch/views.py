from django.shortcuts import render, redirect
from pythonbatch.models import Students
from pythonbatch.form import StudentForm


# Create your views here.
def applandingpage(request):
    if request.method == "POST":
        sform = StudentForm(request.POST)
        if sform.is_valid(): #validation
            try:
                sform.save()
                return redirect('/show')
            except:
                pass
    else:
        sform = StudentForm()
    return render(request,'index.html',{'form':sform})


def show(request):
    studlist = Students.objects.all()
    return render(request,"show.html",{'studentlist':studlist})


def edit(request,econtact):
    studrecord = Students.objects.get(econtact=econtact)
    return render(request,'edit.html', {'singleStud':studrecord})


def update(request, econtact):
    stud = Students.objects.get(econtact = econtact)
    sform = StudentForm(request.POST, instance = stud)
    if sform.is_valid():
        sform.save()
        return redirect("/show")
    return render(request, 'edit.html', {'singleStud': stud})

def destroy(request,first_name):
    stud = Students.objects.get(first_name=first_name)
    stud.delete()
    return redirect("/show")