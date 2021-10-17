from django.urls import path

from .views import NegocioListView, NegocioDetailView
from . import views


urlpatterns = [
    
   
    path('', NegocioListView.as_view(), name='negocio_list'),
    path('<slug:slug>', NegocioDetailView.as_view(), name='negocio_detail'),

]