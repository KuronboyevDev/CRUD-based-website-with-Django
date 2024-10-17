from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
# from django.contrib.auth import logout as auth_logout
# from django.shortcuts import redirect
# from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile


class EditProfilePageView(generic.UpdateView):
  model = Profile
  template_name = 'registration/edit_profile_page.html'
  fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'telegram_url' ]
  success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
   model = Profile
   template_name = 'registration/user_profile.html'
   
   def get_context_data(self, *args, **kwargs):  
    users = Profile.objects.all()
    context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
   
    page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
   
    context["page_user"] = page_user
    return context
 
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    model = User
    

    def get_object(self):
         return self.request.user
    
    
    
def LogoutView(request):
    logout(request)
    return redirect('login')
  

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             success_url = reverse_lazy('home')
        
#         else:
       
#             print("There is a problem")
