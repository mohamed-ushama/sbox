from django import forms
from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['sender_name', 'receiver_name', 'file_upload']

class DownloadFileForm(forms.Form):
    file_id = forms.IntegerField(label='File ID')
