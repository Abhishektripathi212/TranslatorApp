from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from main.models import TranslateText


class TranslationAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_translation_api(self):
        """
        Positive test case with all the required parameters.
        """
        data = {
            'from_language': 'english',
            'to_language': 'spanish',
            'original_text': 'Hello, world!'
        }

        response = self.client.get('/api/translate-text/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the translation was stored in the database
        translation = TranslateText.objects.get()
        self.assertEqual(translation.from_language, data['from_language'])
        self.assertEqual(translation.to_language, data['to_language'])
        self.assertEqual(translation.original_text, data['original_text'])
        self.assertIsNotNone(translation.translated_text)

    def test_translation_api_missing_fields(self):
        """
        Test case where one of the parameter is missing
        """

        data = {
            'from_language': 'english',
            'to_language': 'spanish',
            # Missing 'original_text' field
        }

        response = self.client.get('/api/translate-text/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_translation_api_empty_text(self):
        """
        Test case where original text in blank then response data should also be blank.
        """

        data = {
            'from_language': 'english',
            'to_language': 'korean',
            'original_text': '',
        }

        response = self.client.get('/api/translate-text/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_translation_api_invalid_endpoint(self):
        """
        Test case to check api end point.
        """

        data = {
            'from_language': 'english',
            'to_language': 'french',
            'original_text': 'Hello, world!'
        }

        response = self.client.get('/api/invalid_endpoint/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
