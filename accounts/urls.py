from accounts.views import (
    LoginView,
    PasswordResetConfirmView,
    PasswordResetView, RegistrationView, AccountDetailView,
)
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('register/', RegistrationView.as_view(), name='register'),


    path('profile/<int:pk>/', AccountDetailView.as_view(), name='profile'),




    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]