from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Item1", price=10)
        Menu.objects.create(title="Item2", price=15)

    def test_getall(self):
        response = self.client.get("http://localhost:8000/restaurant/menu/")

        self.assertEqual(response.status_code, 200)

        expected_data = [
            {"title": "Item1", "price": "10.00"},
            {"title": "Item2", "price": "15.00"},
        ]
        
        self.assertQuerysetEqual(
            response.data,
            expected_data,
            transform=lambda x: {"title": x["title"], "price": x["price"]},
        )
