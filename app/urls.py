from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<slug:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<slug:pk>/', views.delete_student, name='delete_student'),
]