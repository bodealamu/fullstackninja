from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class DashboardTests(TestCase):

    def setup(self):
        self.user = get_user_model().objects.create_superuser( email='testuser@email.com',
            password='secret',
            first_name='test',
            last_name='user',
        )

    def test_dashboard_page_status_code(self):
        self.client.login(email='testuser@email.com', password='secret')
        response = self.client.get('/dashboard/')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_category_status_code(self):
        response = self.client.get('/dashboard/category')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_staff_status_code(self):
        response = self.client.get('/dashboard/staff')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_subategory_status_code(self):
        response = self.client.get('dashboard/subcategory')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_tutorialseries_status_code(self):
        response = self.client.get('dashboard/tutorialseries')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_tutorialvideos_status_code(self):
        response = self.client.get('dashboard/tutorialvideos')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_profile_status_code(self):
        response = self.client.get('dashboard/profile')
        self.assertEqual(first=response.status_code, second=200)

    def test_dashboard_messages_status_code(self):
        response = self.client.get('dashboard/messages')
        self.assertEqual(first=response.status_code, second=200)
