from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('webservice/', views.webservice, name='webservice')
]
