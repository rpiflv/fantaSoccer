from django.test import TestCase

class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_teams_page_status_code(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, 200)
