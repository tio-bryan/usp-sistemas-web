from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import File
from .forms import FileForm


def index(request):
    all_files = File.objects.filter(owner=request.user.id)
    form = FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('teste' + str(request.user.id))
        form.save()
        return HttpResponseRedirect('/')
      
    return render(request, 'drive.html', {'form': form, 'all_files': all_files})

def remove(request, id):
    File.objects.filter(id=id).delete()
    

    return HttpResponseRedirect('/')