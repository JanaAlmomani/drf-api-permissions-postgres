from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack


# Create your tests here.

class SnackTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Snack.objects.create(title='chips', purchaser=testuser1, description="test desc ...")
        test_thing.save()

    def snacks_model(self):
        snack = Snack.objects.get(id=1)
        actual_purchaser= str(Snack.purchaser)
        actual_title = str(Snack.title)
        actual_description = str(Snack.description)
        self.assertEqual(actual_purchaser,"testuser1")
        self.assertEqual(actual_title,"chips")
        self.assertEqual(actual_description,"test desc ...")