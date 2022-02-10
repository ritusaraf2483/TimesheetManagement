from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from usermanagement.forms import ProfileForm
from usermanagement.models import Profile


class UsersList(ListView):
    model = Profile
    template_name = 'users/users_list.html'


class ProfileDetail(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profiles_new.html'
    success_url = reverse_lazy("Users:userslist")
    login_url = 'Users:login'

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model=Profile
    form_class = ProfileForm
    template_name = 'users/profile_update.html'
    success_url = reverse_lazy("Users:userslist")
    login_url = 'Users:login'

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'users/profile_delete.html'
    success_url = reverse_lazy("Users:userslist")
    login_url = 'Users:login'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})