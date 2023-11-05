from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.vote, name='vote'),
    path('api',views.varify,name="heh"),
    path('getre',views.getre,name="getre"),
    #getre
]

