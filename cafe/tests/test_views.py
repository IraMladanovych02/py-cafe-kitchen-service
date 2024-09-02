from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from cafe.models import DishType, Dish

DISH_TYPE_URL = reverse('cafe:dish-types-list')
DISH_URL = reverse('cafe:dish-list')


class PublicTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='test123',
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        DishType.objects.create(name="salad")
        DishType.objects.create(name="pasta")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_types_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, 'cafe/dish_types_list.html')

    def test_retrieve_dish(self):
        dish_type = DishType.objects.create(name="Main Course")
        Dish.objects.create(name="pizza", price="10.50", dish_type=dish_type)
        Dish.objects.create(name="Karbonara", price="12.50", dish_type=dish_type)

        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, 'cafe/dish_list.html')
