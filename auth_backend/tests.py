from django.test import TestCase
from auth_backend.backends import (
    BaseSurveyAdminManager,
    CustomTokenSerializer,
    SimpleAuthBackend,
)
from accounts.models import SurveyAdmin

# Create your tests here.


class AuthBackendTestCase(TestCase):

    def setUp(self) -> None:
        self.admin = BaseSurveyAdminManager.create_survey_admin(
            username="testuser", password="123456"
        )

    def test_if_user_is_created(self):
        """
        Test the base survey admin manager for user creation
        """
        survey_admin = SurveyAdmin.objects.get(username=self.admin.username)
        self.assertEqual(survey_admin, self.admin)

    def test_hashing(self):
        """
        test if the passwd has been succeshfully hashed
        """
        self.assertNotEqual("123456", self.admin.password)


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.admin = BaseSurveyAdminManager.create_survey_admin(
            username="testuser", password="123456"
        )
        self.auth = SimpleAuthBackend

    def test_user_auth(self):
        """
        test if authentication works
        """
        survey_admin = self.auth.authenticate(self.admin.username, "123456")
        self.assertEqual(survey_admin, self.admin)

    def test_login_fail(self):
        survey_admin = self.auth.authenticate(self.admin.username, "10000")
        self.assertEqual(survey_admin, None)


class TestTokenLogin(TestCase):

    def setUp(self) -> None:
        self.token_serializer = CustomTokenSerializer()
        self.admin = BaseSurveyAdminManager.create_survey_admin(
            username="testuser", password="123456"
        )

    def test_token_login(self):
        response = self.token_serializer.login_admin(
            request=None, survey_admin=self.admin
        )
        self.assertTrue(response.__contains__("access"))
        self.assertTrue(response.__contains__("refresh"))
