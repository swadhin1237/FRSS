from django.test import TestCase,Client
from django.urls import reverse
from shop.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(username="avenger")
        self.test_user.set_password("venky")
        self.test_review = Review.objects.create(user_id="1", product_id="1", user_review="This is nice product", user_name="avenger")
        self.test_cust = Customer.objects.create(user=self.test_user, first_name="avenger", last_name="assemble", email="venk@gmail.com",phone="90897")
        self.test_prod = Product.objects.create(product_name="bed" ,category="Furniture",
                                                sub_category="bed",
                                                price="12344",
                                                currentNumber="23",
                                                totalNumber="123",
                                                product_desc="A nice bed",
                                                pub_date="2005-12-20",
                                                color="brown")
    def test_index(self):
        response = self.client.get(reverse('ShopHome',args=[self.test_user.id]))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop/index.html')

    def test_change_password(self):
        self.client.login(username="avenger",password="venky")
        response = self.client.post(reverse('change_password',args=[1]),{'current_password':'venky','new_password':'swadhin'})

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'shop/change_password.html')

    def test_review(self):
        response = self.client.post(reverse('review', args=[self.test_prod.id,self.test_cust.user.id]), {'cust_review': str(self.test_review.user_review)})
        self.assertEquals(response.status_code, 302)

    def test_payment(self):
        response = self.client.post(reverse('payment', args=[self.test_cust.user.id]), {'credit_card_number':"123",
                                                                                        'month':"feb",
                                                                                        'year':"2022",
                                                                                        'cvv':"212",
                                                                                        'payment':"23400"})
        self.assertEquals(response.status_code, 302)
    def test_payment2(self):
        response = self.client.get(reverse('payment2', args=[self.test_cust.user.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'shop/payment.html')

    def test_editProfile2(self):
        response = self.client.get(reverse('editProfile2', args=[self.test_cust.user.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'shop/editprofile.html')

    def test_editProfile(self):
        response = self.client.post(reverse('editProfile', args=[self.test_cust.user.id]), {'first_name':"we" ,'last_name':"rt",'email':"sd@gmail.com",'phone':"1234"})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'shop/editprofile.html')

    def test_about(self):
        response = self.client.get(
            reverse('AboutUs', args=[self.test_user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/about.html')

    def test_contact(self):
        response = self.client.get(
            reverse('ContactUs', args=[self.test_user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/contact.html')

    def test_learn(self):
        response = self.client.get(reverse('Learn'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/learn.html')

    def test_tracker(self):
        response = self.client.get(reverse('Tracker'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/tracker.html')

    def test_log_in(self):
        response = self.client.post(
            reverse('log_in'), {'username': 'avenger', 'password': 'venky'})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/login.html')

    def test_signup(self):
        response = self.client.post(reverse('signup'), data={
            'username': 'swadhinbitch',
            'first_name': 'swadhin',
            'last_name': 'majhi',
            'email': 'kyapata',
            'phone': '69',
            'password': 'kyapata',
            'confirm_password': 'kyapata'})

        self.assertEquals(response.status_code, 302)
        users = User.objects.all()
        self.assertEqual(users.count(), 2)

    def test_product_view(self):
        response = self.client.get(
            reverse('ProductView', args=[self.test_prod.id, self.test_cust.user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/prodView.html')

    def test_checkout(self):
        response = self.client.get(
            reverse('Checkout', args=[self.test_cust.user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/checkout.html')

    def test_histpry(self):
        response = self.client.get(
            reverse('history', args=[self.test_cust.user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/history.html')

    def test_explore(self):
        response = self.client.get(reverse('explore'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/demoview.html')

    def test_profile(self):
        response = self.client.get(
            reverse('profile', args=[self.test_cust.user.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/profile.html')

    def test_logout(self):
        response = self.client.get(reverse('logout'))

        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response,'shop/checkout.html')
