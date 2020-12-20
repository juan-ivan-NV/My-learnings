from django.urls import path
from wpa import views

urlpatterns = [
    path('',views.home, name="Homepage"),
    path('services',views.services, name="Services"),
    path('store',views.store, name="Store"),
    path('blog',views.blog, name="Blog"),
    path('contact',views.contact, name="Contact"),
]