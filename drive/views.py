from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import File
from .forms import FileForm


def index(request):
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('teste')
        form.save()
        return HttpResponseRedirect('/')
      
    return render(request, 'drive.html', {'form': form})