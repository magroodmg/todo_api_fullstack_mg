from rest_framework import serializers

from .models import User

# define Class Serialize User List
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)   # write_only จะไม่เห็นตอนพิมพ์
    # Class meta เพื่อระบุ model และ fields ที่ต้องการ Serialize
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password",
            "is_active"
        )

    def create(self, validated_data):  # ในการ Create User จำเป็นต้องมี def นี้เพื่อให้ comply กับมาตรฐาน Auth ของ Django
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

# define Class Serialize User Detail
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "is_active",
            "last_login",
        )