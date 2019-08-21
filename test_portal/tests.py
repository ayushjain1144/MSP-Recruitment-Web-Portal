from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import register,login

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='mohul', email='m@gmail.com', password='mohul44')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/register')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()


        response = register(request)
 
        self.assertEqual(response.status_code, 200)