from rest_framework import generics
from rest_framework.permissions import IsAdminUser # Import for check AdminUser

from .serializers import UserSerializer, UserDetailSerializer # API เป็น JSON ต้องผ่านการ Serialize จาก serializers.py
from .models import User

# User List ทั้งหมด
class UserListCreateView(generics.ListCreateAPIView):       # Create View ดู และ สร้าง
    permission_classes = [IsAdminUser]      # Permission for Admin only (User List Create View)
    queryset = User.objects.all()
    serializer_class = UserSerializer   # Serialize User

# User Detail ราย user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):        # Retrive เรียก Update แก้ไข Destroy ลบ View ดู
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer     # Serialize User Detail