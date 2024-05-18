from django.urls import path
from . import views

urlpatterns = [
             path('Mlogin/', views.Mlogin),
             path('Mhome/', views.managerpg),

             path('viewoportal/', views.viewoportal),
             path('opapprove/<int:id>/', views.opapprove),
             path('opreject/<int:id>/', views.opreject),

             path('viewSprovider/', views.viewSprovider),
             path('spapprove/<int:id>/', views.spapprove),
             path('spreject/<int:id>/', views.spreject),

             path('viewoutsourcees/', views.viewoutsourcees),
             path('outsourceesapprove/<int:id>/', views.outsourceesapprove),
             path('outsourceesreject/<int:id>/', views.outsourceesreject),

            # path('viewzkpprotocol/', views.viewzkpprotocol),
             #path('zkpprotocolapprove/<int:id>/', views.zkpapprove),
             #path('zkpprotocolreject/<int:id>/', views.zkpreject),

             #path('viewzkpprotocolreport/', views.zkpprotocolreport),
             #path('zkpreportapprove/<int:id>/', views.zkpreportapprove),
             #path('zkpreportreject/<int:id>/', views.zkpreportreject),

             path('viewcontractdata/', views.contractdata),
             path('contractapprove/<int:id>/', views.contractapprove),
             path('contractreject/<int:id>/', views.contractreject),
             path('contractreject/<int:id>/', views.contractreject),
             path('viewcomplaint/', views.complaintdata),
             path('complaintinspect/<int:id>/', views.complaintinspect),
             path('sendsolution/', views.sendingsolution),
             path('sentsolution/<int:id>/', views.sentsolution),

]