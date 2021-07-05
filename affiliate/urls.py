from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),    
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('search/', views.search_courses, name='search')
]