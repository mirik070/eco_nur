from django.urls import path

from user.views import LoginView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home-view"),
    path('login/', LoginView.as_view(), name="login-view"),
]
