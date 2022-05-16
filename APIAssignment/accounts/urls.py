from django.urls import path
from accounts.views import RegisterAPI
from rest_framework.authtoken import views


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name = "registerapi"),
    path('api/login/', views.obtain_auth_token),
    ]   