from django.test import TestCase
from django.urls import reverse

class AffiliateTest(TestCase):

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.min.html')
