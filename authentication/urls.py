from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='users'),

    # Authentication
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('verify/', views.VerifyUserView.as_view(), name='verify'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('refresh-token/', views.RefreshTokenView.as_view(), name='refresh-token'),
    path('profile/', views.TestAuthenticationView.as_view(), name='profile'),

    # Password reset
    path('password-reset/', views.PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('set-new-password/', views.SetNewPassword.as_view(), name='set-new-password'),

    path('logout/', views.LogoutUserView.as_view(), name='logout'),
]
