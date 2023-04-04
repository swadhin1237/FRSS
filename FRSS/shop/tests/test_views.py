from django.test import TestCase,Client
from django.urls import reverse
from shop.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(username="avenger")
        self.test_user.set_password("venky")



    def test_index(self):
        response = self.client.get(reverse('ShopHome',args=[self.test_user.id]))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop/index.html')

    def test_change_password(self):
        self.client.login(username="avenger",password="venky")
        response = self.client.post(reverse('change_password',args=[1]),{'current_password':'venky','new_password':'swadhin'})

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'shop/change_password.html')
