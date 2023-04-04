from django.test import TestCase
from django.urls import resolve,reverse 
from shop.views import *


class TestUrls(TestCase):

    def test_about_us_resolved(self):
        url = reverse('AboutUs',args=[3])
        self.assertEquals(resolve(url).func,about)

    def test_productView_resolved(self):
        url = reverse('ProductView', args=[3,4])
        self.assertEquals(resolve(url).func, productView)

    def test_shophome_resolved(self):
        url = reverse('ShopHome',args=[3])
        self.assertEquals(resolve(url).func,index)

    def test_contact_resolved(self):
        url = reverse('ContactUs', args=[3])
        self.assertEquals(resolve(url).func, contact)

    def test_checkout_resolved(self):
        url = reverse('Checkout', args=[3])
        self.assertEquals(resolve(url).func, checkout)

    def test_learn_resolved(self):
        url = reverse('Learn')
        self.assertEquals(resolve(url).func, learn)

    def test_signup_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_login_resolved(self):
        url = reverse('log_in')
        self.assertEquals(resolve(url).func, log_in)
################################################

    def test_history_resolved(self):
        url = reverse('history', args=[3])
        self.assertEquals(resolve(url).func, history)

    def test_explore_resolved(self):
        url = reverse('explore')
        self.assertEquals(resolve(url).func, explore)

    def test_profile_resolved(self):
        url = reverse('profile', args=[3])
        self.assertEquals(resolve(url).func, profile)

    def test_logout_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, log_out)

    def test_checkout_resolved(self):
        url = reverse('Checkout', args=[3])
        self.assertEquals(resolve(url).func, checkout)

    def test_editProfile_resolved(self):
        url = reverse('editProfile',args=[3])
        self.assertEquals(resolve(url).func, editProfile)

    def test_editProfile2_resolved(self):
        url = reverse('editProfile2', args=[3])
        self.assertEquals(resolve(url).func, editProfile2)

    def test_payment_resolved(self):
        url = reverse('payment',args=[3])
        self.assertEquals(resolve(url).func, payment)

    def test_change_password_resolved(self):
        url = reverse('change_password',args=[3])
        self.assertEquals(resolve(url).func, change_password)

    def test_payment2_resolved(self):
        url = reverse('payment2', args=[3])
        self.assertEquals(resolve(url).func, payment2)

    def test_review_resolved(self):
        url = reverse('review', args=[3,5])
        self.assertEquals(resolve(url).func, review)
#############################################