from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
          path('',views.mainpage),
          path('OPregister/', views.OPregister),
          path('OPlogin/', views.OPlogin),
          path('OPlogout/', views.OPlogout),
          path('mainpg/', views.mainpage),
          path('ophome/', views.oportalhome),
          path('opreq/', views.oportalrequirement),
          path('spdata/', views.SPdata),
          path('contract/', views.contract),
          path('addcontract/<str:spid>/', views.addcontract),
          path('negotime/', views.negotime),
          path('sendnegotime/<int:id>/', views.sendnegotime),
          path('uploaddataset/', views.uploaddataset),
          path('senddataset/', views.senddataset),
          path('senddata/<str:spid>/', views.sentdata),
          path('download/',views.download)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



