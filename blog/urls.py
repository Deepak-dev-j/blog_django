from django.urls import path
from . import views

app_name="blog"

urlpatterns=[
    path("", views.index,name="index"),
    path("plan/<int:plan_id>",views.plan,name="plan"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("old_url",views.old_url_redirect,name="old_url"),
    path("new_something_url",views.new_url_view,name="new_page_url"),
    path("contact",views.contact_view,name="contact"),
    path("about",views.about_view,name="about"),

    ]