from django.urls import path
from django.contrib.auth import views as auth_views
from usermanagement import views

app_name = 'Users'
urlpatterns=[
    path('userslist',views.UsersList.as_view(),name='userslist'),

    path('new',views.ProfileCreate.as_view()),
    path('<pk>/update',views.ProfileUpdate.as_view()),
    path('<pk>/delete',views.ProfileDelete.as_view()),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logged_out.html'),name='logout'),
    path('signup',views.signup,name='signup'),
    path('<pk>',views.ProfileDetail.as_view(),name='profiledetail'),
]