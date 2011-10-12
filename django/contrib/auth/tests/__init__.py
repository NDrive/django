from django.conf import settings
from django.test import TestCase
class BaseTestCase(TestCase):
    backend = 'django.contrib.auth.backends.ModelBackend'
    def setUp(self):
        self.curr_auth = settings.AUTHENTICATION_BACKENDS
        settings.AUTHENTICATION_BACKENDS = (self.backend,)

    def tearDown(self):
        settings.AUTHENTICATION_BACKENDS = self.curr_auth


from django.contrib.auth.tests.auth_backends import (BackendTest,
    RowlevelBackendTest, AnonymousUserBackendTest, NoAnonymousUserBackendTest,
    NoBackendsTest, InActiveUserBackendTest, NoInActiveUserBackendTest)
from django.contrib.auth.tests.basic import BasicTestCase
from django.contrib.auth.tests.decorators import LoginRequiredTestCase
from django.contrib.auth.tests.forms import (UserCreationFormTest,
    AuthenticationFormTest, SetPasswordFormTest, PasswordChangeFormTest,
    UserChangeFormTest, PasswordResetFormTest)
from django.contrib.auth.tests.remote_user import (RemoteUserTest,
    RemoteUserNoCreateTest, RemoteUserCustomTest)
from django.contrib.auth.tests.models import ProfileTestCase
from django.contrib.auth.tests.signals import SignalTestCase
from django.contrib.auth.tests.tokens import TokenGeneratorTest
from django.contrib.auth.tests.views import (PasswordResetTest,
    ChangePasswordTest, LoginTest, LogoutTest, LoginURLSettings)
from django.contrib.auth.tests.permissions import TestAuthPermissions

# The password for the fixture data users is 'password'
