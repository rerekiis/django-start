from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.person_create, name='person_create'),
    path('list/', views.person_list, name='person_list')
]