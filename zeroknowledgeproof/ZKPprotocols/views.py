from django.shortcuts import render,redirect

from django.contrib import messages
from .models import File
from .forms import FileForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import DownloadFileForm
from .models import File

def view_files(request):
    files = File.objects.all()
    return render(request, 'files/view_files.html', {'files': files})
from django.shortcuts import render


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " File Uploaded successfully for check click view")
            return redirect('/uload/')  # Redirect to the same page after successful upload
    else:
        form = FileForm()
    return render(request, "files/upload_file.html", {'form': form})

def download_file(request):
    if request.method == 'POST':
        form = DownloadFileForm(request.POST)
        if form.is_valid():
            file_id = form.cleaned_data['file_id']
            file_obj = get_object_or_404(File, pk=file_id)
            file_path = file_obj.file_upload.path
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=' + file_obj.file_upload.name
                return response
    else:
        form = DownloadFileForm()
    return render(request, 'files/download.html', {'form': form})

# Create your views here.
