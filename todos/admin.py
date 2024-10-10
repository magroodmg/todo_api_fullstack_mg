from django.contrib import admin

from .models import Todo

admin.site.register(Todo) # ใส่ Todo model ของ todos app ใน admin site เพื่อสามารถตรวจสอบและแก้ไขได้