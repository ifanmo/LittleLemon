from django.test import TestCase
from .models import Menu

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Cake', price=80, inventory=100)
        self.assertEqual(item, "Cake : 80")
