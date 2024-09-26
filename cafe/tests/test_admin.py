from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.cook = self.admin_user = get_user_model().objects.create_user(
            username="cook", password="testcook", years_of_experience=2
        )

    def test_cook_years_of_experience_listed(self):
        """ "
        Test that cook`s years of experience is listed in list_display on cook admin page
        """
        url = reverse("admin:index")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)
