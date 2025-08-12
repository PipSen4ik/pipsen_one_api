from django.urls import path
from . import views

urlpatterns = [
    path('get-projects/', views.get_projects, name='get_projects'),
    path('get-project/<int:pk>/', views.get_project, name='get_project'),
]