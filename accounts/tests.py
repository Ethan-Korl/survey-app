from django.test import TestCase, Client
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from auth_backend.tests import AuthBackendTestCase, TestTokenLogin, TestAuthentication
from accounts.models import SurveyAdmin
from accounts.repository import SurveyAdminRepository


# Run auth backend test case here
AuthBackendTestCase

# test auth
TestAuthentication

# user token login
TestTokenLogin


class SurveyAdminRepositoryTests(TestCase):

    def setUp(self):
        # Create a test SurveyAdmin instance
        self.admin = SurveyAdmin.objects.create(
            username="testuser", password=make_password("password123")
        )

    def test_get_by_id_success(self):
        admin = SurveyAdminRepository.get_by_id(self.admin.id)
        self.assertEqual(admin, self.admin)

    def test_get_by_id_not_found(self):
        admin = SurveyAdminRepository.get_by_id("d9436186-fd1c-4f79-a61f-9ce87617e760")
        self.assertIsNone(admin)

    def test_get_by_username_success(self):
        admin = SurveyAdminRepository.get_by_username(self.admin.username)
        self.assertEqual(admin, self.admin)

    def test_get_by_username_not_found(self):
        admin = SurveyAdminRepository.get_by_username("nonexistentuser")
        self.assertIsNone(admin)

    def test_create(self):
        admin = SurveyAdminRepository.create("newuser", make_password("newpassword"))
        self.assertEqual(admin.username, "newuser")
        self.assertTrue(admin.check_password("newpassword"))

    def test_delete_success(self):
        result = SurveyAdminRepository.delete(self.admin.id)
        self.assertTrue(result)
        self.assertIsNone(SurveyAdminRepository.get_by_id(self.admin.id))

    def test_delete_not_found(self):
        result = SurveyAdminRepository.delete("nonexistent_id")
        self.assertFalse(result)


class AccountsViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_if_page_renders(self):
        url = reverse("accounts:login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_login.html")

    def test_if_page_renders(self):
        url = reverse("accounts:signup")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sa_register.html")
