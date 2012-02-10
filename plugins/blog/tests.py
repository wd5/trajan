from django.test import TestCase


# View testing.

class ViewTest(TestCase):
     def test_home(self):
        response = self.client.get('/widget/')
        self.assertEqual(response.status_code, 200)