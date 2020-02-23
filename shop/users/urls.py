from django.urls import path
from users import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('verify-email', views.verify_view)
]