from django.test import TestCase
from django.test import Client
from django.test import override_settings

from .models import Medicine

class BaseViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

class MedicineModelTestCase(TestCase):
    def setUp(self):
        Medicine.objects.create(key="key1", value="value1")
        Medicine.objects.create(key="key2", value="value2")

    def test_record_creation(self):
        medicine1 = Medicine.objects.get(key="key1")
        medicine2 = Medicine.objects.get(key="key2")
        self.assertEqual(medicine1.value, 'value1')
        self.assertEqual(medicine2.value, 'value2')

class MedicineListViewTestCase(BaseViewTestCase):
    def setUp(self):
        super().setUp()
        Medicine.objects.create(key="key1", value="value1")
        Medicine.objects.create(key="key2", value="value2")
        Medicine.objects.create(key="key3", value="value3")

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(len(response.context['keys']),3)
        self.assertEqual(response.status_code, 200)

class MedicineResultViewTestCase(BaseViewTestCase):
    def setUp(self):
        super().setUp()
        Medicine.objects.create(key="key1", value="key1")
        Medicine.objects.create(key="key2", value="key1")
        Medicine.objects.create(key="key3", value="key1")
        Medicine.objects.create(key="key4", value="zzzz")

    def test_index(self):
        response = self.client.get('/search/', {'keys': 'key1'})
        self.assertEqual(len(response.context['result']),3)
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