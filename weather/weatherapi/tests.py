from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class WeatherTests(APITestCase):
    def test_get_weather(self):

        url = reverse('weather')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(url, data={'location':'test'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.get(url, data={'day': 9})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(url, data={'location':'weather-kyiv-4944'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(url, data={ 'day': 9, 'location':'weather-kyiv-4944'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_another_methods_weather(self):

        url = reverse('weather')
        response = self.client.put(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.post(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)