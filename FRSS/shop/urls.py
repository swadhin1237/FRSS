from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("<int:user1_id>", views.index, name="ShopHome"),
    path("about/<int:user1_id>", views.about, name="AboutUs"),
    path("contact/<int:user1_id>", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Tracker"),
    path("products/<int:id>/<int:user1_id>", views.productView, name="ProductView"),
    path("checkout/<int:user1_id>", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("learn/",views.learn,name="Learn"),
    path("signup/", views.signup, name="signup"),
    path("log_in", views.log_in, name="log_in"),
    path("history/<int:user1_id>", views.history, name='history')
]
