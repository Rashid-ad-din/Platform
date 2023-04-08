from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import path

from accounts.views.accounts import AccountCreateView, logout_view

urlpatterns = [
    path('register/account/<str:type>/', AccountCreateView.as_view(), name='account_register'),
    path('account/<int:pk>/change-password/', PasswordChangeView.as_view(), name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(), name='login_page'),
]
