from django.test import TestCase

from solos.models import Solo


class SoloModelTest(TestCase):

    def setUp(self):
        self.solo = Solo.objects.create(
            track='Falling in Love with Love',
            artist='Oscar Peterson',
            instrument='piano',
            album='At the Stratford Shakespearean Festival',
            start_time='1:24',
            end_time='4:06'
        )

    def test_solo_basic(self):
        """
        Test the basic functionality of Solo
        """
        self.assertEqual(self.solo.artist, 'Oscar Peterson')
        self.assertEqual(self.solo.end_time, '4:06')
