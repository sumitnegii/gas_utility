from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ServiceRequest

class ServiceRequestTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@user.com',
            password='testpass123'
        )

    def test_request_creation(self):
        request = ServiceRequest.objects.create(
            customer=self.user,
            request_type='LEAK',
            description='Gas smell in kitchen'
        )
        self.assertEqual(request.status, 'SUBMITTED')
        self.assertEqual(str(request), 'Gas Leak - test@user.com')