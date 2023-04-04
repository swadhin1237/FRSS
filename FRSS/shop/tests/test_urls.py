from django.test import TestCase
from django.urls import resolve,reverse 
from shop.views import *


class TestUrls(TestCase):

    def test_about_us_resolved(self):
        url = reverse('AboutUs',args=[3])
        self.assertEquals(resolve(url).func,about)

    def test_about_us_resolved(self):
        url = reverse('ProductView', args=[3,4])
        self.assertEquals(resolve(url).func, productView)






