from django.urls import path
from django.contrib.auth import views as auth_views
from usermanagement import views

app_name = 'Users'
urlpatterns=[
    path('userslist',views.users_list.as_view(),name='userslist'),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logged_out.html'),name='logout'),
    path('signup',views.signup,name='signup')
]