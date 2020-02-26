from django.urls import path

from landing import views

urlpatterns = [
    path('', views.landing_view),
    path('about', views.about_view),
    path('main', views.landing_view),
    path('checkout', views.checkout),
    path('contacts', views.contacts)
    ]