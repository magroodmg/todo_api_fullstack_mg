from django.urls import path

from.views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/",DetailTodo.as_view(),name="todo_detail"),      # api/todos/<id> ทำให้สามารถเข้าไปดู todo ราย id ได้
    path("",ListTodo.as_view(),name="todo_list"),       # api/todos โชว์ list ทั้งหมด
]
