from django.contrib.auth import get_user_model
from django.test import TestCase

from cafe.models import DishType, Dish


class ModelTests(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Test")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Test")
        dish = Dish.objects.create(name="Test", price=10.50, dish_type=dish_type)
        self.assertEqual(str(dish), f"{dish.name} ({dish.price}, {dish.dish_type})")

    def test_create_cook_including_years_of_experience(self):
        username = "Test"
        password = "test123"
        years_of_experience = 2
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
