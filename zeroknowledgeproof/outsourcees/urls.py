from django.urls import path
from . import views

urlpatterns = [
          path('outsourcesregister/', views.outsourceesregister),
          path('outsourcelogin/', views.outsourceeslogin),
          path('outsourcelogout/', views.outsourceeslogout),
          path('mainpg/', views.mainpage),
          path('outsourcehome/', views.outsourceeshome),
          path('viewcompanies/', views.viewcompanies),
          path('viewSP/', views.viewSP),
          path('viewnegotime/', views.ntimeoutsoourcees),
          path('viewspdata/', views.viewspdata),
          path('complaintsp/', views.spcomplaint),
          path('makecomplaint/<int:id>/', views.makecomplaintsp),
]