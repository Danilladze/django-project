from django.contrib.auth import get_user_model,authenticate
from django.test import TestCase, Client
from .models import link
from .views import create,signup,link_show,home


class SignInTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username = 'testUser', password = 'testPassword')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='testUser', password='testPassword')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testPassword')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='testUser', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

class linkTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username = 'testUser', password = 'testPassword')
        self.user.save()
        self.link = link(link = 'https://google.com/')
        self.link.save()

    def tearDown(self):
        self.user.delete()

    def test_link_input(self):
        self.assertEqual(self.link.link,'https://google.com/')

    def test_update_link(self):
        self.link.link = 'https://yandex.ru'
        self.link.save()
        self.assertEqual(self.link.link,'https://yandex.ru')

