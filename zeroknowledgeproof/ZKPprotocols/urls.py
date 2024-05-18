from django.urls import path
from .import views

urlpatterns = [
    path('dload/', views.download_file),
    path('view/', views.view_files),
    path('uload/', views.upload_file),

]