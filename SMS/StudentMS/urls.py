from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/', views.student_list, name="student_list"),

]