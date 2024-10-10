# Test APP ด้วยการใช้ coding

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Todo

# Todo Model Test
class TodoModelTest(TestCase):
    @classmethod
    # สร้างข้อมูลตัวอย่าง
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "first todo",
            body="this is body"
        )
    
    # check title == "first todo"
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_title = f"{todo.title}"
        self.assertEqual(expected_title,"first todo")

    # check content == "this is body"
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_body = f"{todo.body}"
        self.assertEqual(expected_body,"this is body")

    # check todo list
    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))    # get todo_list จากชื่อ url name ใน urls.py
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # check HTTP response code
        self.assertEqual(Todo.objects.count(),1)    # check HTTP activities count
        self.assertContains(response, self.todo)    # check ว่าใน todo_list มี self.todo(test data ที่พึ่งสร้าง)
    
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),    # get todo_detail จากชื่อ url name และ kwargs ที่ id ของ test data (id=1)
            format="json"   # ระบุ format JSON
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # check HTTP response code
        self.assertEqual(Todo.objects.count(),1)    # check HTTP activities count
        self.assertContains(response, "first todo")  # check todo_detail มี string "first todo" อยู่ใน value(JSON) ใดซักอัน