from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
          path('SPregister/', views.SPregister),
          path('SPlogin/', views.SPlogin),
          path('SPlogout/', views.SPlogout),
          path('SPhome/', views.SPhome),

          path('viewpost/', views.viewpost),

          path('SPmessage/', views.SPmessage),
          path('SPaccept/<int:id>/', views.SPaccept),
          path('SPrequest/<int:id>/', views.SPrequest),
          path('viewspagree/', views.SPagreecontract),
          path('spagree/<int:id>/', views.SPagree),
          path('spprovidedata/', views.spprovidedata),
          path('spleakeddata/<int:id>/', views.spleakeddata),
          path('spuploaddata/', views.spuploaddata),
          path('spsenddata/', views.spsendingdata),
          path('spgavedata/<int:id>/', views.spgavedata),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

