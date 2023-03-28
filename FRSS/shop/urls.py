from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Tracker"),
    path("products/<int:id>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("search/", views.search, name="Search"),
    path("learn/",views.learn,name="Learn")
]
