from django.urls import path
from wpa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Homepage"),
    path('services',views.services, name="Services"),
    path('store',views.store, name="Store"),
    path('blog',views.blog, name="Blog"),
    path('contact',views.contact, name="Contact"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)