from django.core.urlresolvers import resolve
from django.test import TestCase

from solos.views import index


class SolosURLsTests(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Test that the root url of the site resolves to the correct view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)
