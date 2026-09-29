from django.test import SimpleTestCase


class PackagingSanityTests(SimpleTestCase):
    def test_core_app_is_installed(self):
        from django.apps import apps
        self.assertTrue(apps.is_installed("core"))
