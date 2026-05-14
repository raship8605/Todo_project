from django.urls import path
from .import views
urlpatterns = [
   path('tasklist/',views.task_list, name='task_list'),
   path('addtask/',views.add_task,name='add_task'),

]