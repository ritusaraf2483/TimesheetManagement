from django.urls import path
from django.contrib.auth import views as auth_views
from usermanagement import views

app_name = 'Users'
urlpatterns=[
    path('userslist',views.users_list.as_view()),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('signup',views.signup)
]