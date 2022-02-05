from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/', views.student_list, name="student_list"),
    path('student/add/', views.add_student, name="add_student"),
    path('student/<int:student_id>/delete', views.student_delete, name="student_delete"),
    path('leaves/',views.ap_leaves,name="ap_leaves")

]