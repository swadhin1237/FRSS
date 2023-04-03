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
    path("log_in/", views.log_in, name="log_in"),
    path("history/<int:user1_id>", views.history, name='history'),
    path("explore/",views.explore,name='explore'),
    path("profile/<int:user1_id>",views.profile,name="profile"),
    path("logout/",views.log_out,name="logout"),
    path("edit_profile/<int:user1_id>/",views.editProfile,name="editProfile"),
    path("edit_profile2/<int:user1_id>/", views.editProfile2, name="editProfile2"),
    path("change_password/<int:user1_id>/",views.change_password, name="change_password"),
    path("payment/<int:user1_id>/",views.payment, name="payment"),
    path("payment2/<int:user1_id>/", views.payment2, name="payment2")

]
