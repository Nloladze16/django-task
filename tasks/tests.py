from django.test import TestCase
from django.urls import reverse
from .models import Task

# Create your tests here.


class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(
            title="Test Task", description="This is a test task."
        )

    def test_model_content(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task.")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Test Task")
        self.assertContains(response, "This is a test task.")
