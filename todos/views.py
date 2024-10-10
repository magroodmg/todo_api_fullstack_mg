from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Todo
from .serializers import TodoSerializer

"""
CRUD Operation
C = Create
R = Read
U = Update
D = Delete
"""
# Todo List ทั้งหมด
class ListTodo(generics.ListCreateAPIView):
    permission_classes =[IsAuthenticatedOrReadOnly]     # auth จะสามารถสร้างได้ แต่ถ้าไม่มี auth จะ read ได้อย่างเดียว
    queryset = Todo.objects.all().order_by('-id')       # order_by('-id') เรียงจาก id มาก>น้อย (ใช้ประโยชน์จาก DJANGO ORM) 
    serializer_class = TodoSerializer

# Todo Detail รายตัว
class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer