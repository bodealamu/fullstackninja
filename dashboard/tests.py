from django.test import TestCase, SimpleTestCase

# Create your tests here.


class DashboardTests(TestCase):
    def test_dashboard_page_status_code(self):
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
