from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title   # เลือกโชว์ title เป็นตัวแทน objects ใน admin app :  http://127.0.0.1:8000/admin/todos/todo/
        