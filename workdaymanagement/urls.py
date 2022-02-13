from django.urls import path, re_path
from workdaymanagement import views
from workdaymanagement.views import WorkdayDelete,WorkdayUpdate

app_name='Workday'
urlpatterns=[
   re_path('^workdaylist$',views.GetList.as_view(),name='workday_list'),
   re_path('^new$',views.WorkdayCreate.as_view(),name="new_workday"),
   re_path('^(?P<pk>[0-9]+)/update$',views.WorkdayUpdate.as_view(),name="workday_edit"),
   re_path('^(?P<pk>[0-9]+)/delete$',WorkdayDelete.as_view(),name="workday_delete"),
   re_path('^report$',views.GenerateReport),
   re_path('^(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name="workday_detail"),
]