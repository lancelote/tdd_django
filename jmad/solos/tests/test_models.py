from django.test import TestCase

from solos.models import Solo


class SoloModelTest(TestCase):

    def setUp(self):
        self.solo = Solo.objects.create(
            track='Falling in Love with Love',
            artist='Oscar Peterson',
            instrument='piano'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
