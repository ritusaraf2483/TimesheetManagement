from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from usermanagement import views

app_name = 'Users'
urlpatterns=[
    re_path('^userslist$',views.UsersList.as_view(),name='userslist'),
    re_path('^new$',views.ProfileCreate.as_view(),name='new'),
    re_path('^(?P<pk>[0-9]+)/update$',views.ProfileUpdate.as_view(),name='profileupdate'),
    re_path('^(?P<pk>[0-9]+)/delete$',views.ProfileDelete.as_view(),name='profiledelete'),
    re_path('^login$',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    re_path('^logout$',auth_views.LogoutView.as_view(template_name='users/logged_out.html'),name='logout'),
    re_path('^signup$',views.signup,name='signup'),
    re_path('^(?P<pk>[0-9]+)$',views.ProfileDetail.as_view(),name='profiledetail'),
]