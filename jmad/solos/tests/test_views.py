from django.test import TestCase, RequestFactory

from solos.views import index


class IndexViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_basics(self):
        """
        Test that index view returns a 200 response and uses the correct template
        """
        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)
