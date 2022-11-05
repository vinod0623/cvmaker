from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile

# Create your views here.
def index(request):  # save and show all resumes
    if request.method == 'POST':
        fm = ProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Successfully Created')
            return redirect('/')
        else:
            messages.warning(request, 'Not Valid!!!')
    else:
        fm = ProfileForm()
    resumes = Profile.objects.all()
    return render (request, 'index.html', {'form':fm, 'resume':resumes})

def resume(request, id): #show resume of requested id
    resumes = Profile.objects.get(pk=id)
    return render(request, 'resume.html', {'resume':resumes})

def deleteResume(request, id): #delete resume
    if request.method == 'POST':
        resume = Profile.objects.get(pk=id)
        resume.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('/')