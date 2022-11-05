from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/<int:id>/', views.resume, name='resume'),
    path('delete/<int:id>/', views.deleteResume, name='delete')
]
