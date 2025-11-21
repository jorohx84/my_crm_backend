from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, ResetPasswordView, AdminResetPasswordView
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset-password/', ResetPasswordView.as_view(), name="reset-password"),
    path('admin-reset-password/', AdminResetPasswordView.as_view(), name='admin-reset-password'),
]