from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
# from .views import custom_logout
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
   path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
   # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
   #  path('logout/', custom_logout, name='logout'),
   path('logout/', views.LogoutView, name='logout'),
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
   
]
