from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.AddShowTask,name='addshowtask'),
    path('update/<int:id>/',views.UpdateTask,name='updatetask'),
    path('<int:id>/',views.DeleteTask,name='deletetask')
]