from django.test import TestCase
from django.test import Client
from django.test import override_settings


class BaseViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

class MedicineListViewTestCase(BaseViewTestCase):
    def setUp(self):
        super().setUp()

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(len(response.context['keys']),2853)
        self.assertEqual(response.status_code, 200)

class MedicineResultViewTestCase(BaseViewTestCase):
    def setUp(self):
        super().setUp()

    def test_index(self):
        response = self.client.get('/search/', {'keys': 'PALIVIZUMAB 100MG INJECTION'})
        self.assertEqual(len(response.context['result']),0)
        self.assertEqual(response.status_code, 200)

class ThrottleApiTests(BaseViewTestCase):

    TESTING_THRESHOLD = '5/min'
    @override_settings(THROTTLE_THRESHOLD=TESTING_THRESHOLD)
    def test_list_check_health(self):
        for _ in range(0, 5):
            self.client.get('')

        response = self.client.get('')
        self.assertEqual(response.status_code, 429)

    @override_settings(THROTTLE_THRESHOLD=TESTING_THRESHOLD)
    def test_result_check_health(self):
        for _ in range(0, 5):
            self.client.get('')

        response = self.client.get('')
        self.assertEqual(response.status_code, 429)