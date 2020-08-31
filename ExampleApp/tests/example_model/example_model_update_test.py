from django.test import TestCase
from django.urls import reverse

class ExampleModelUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_example_model_update_page(self):
        response = self.client.get(reverse('example_model_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'example_model/example_model_update.html')