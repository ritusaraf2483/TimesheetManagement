from django.urls import path, re_path
from workdaymanagement import views
from workdaymanagement.views import WorkdayDelete,WorkdayUpdate

app_name='Workday'
urlpatterns=[
   path('workdaylist',views.GetList.as_view(),name='workday_list'),
   path('new',views.WorkdayCreate.as_view(),name="new_workday"),
   path('<pk>/update',views.WorkdayUpdate.as_view(),name="workday_edit"),
   path('<int:pk>/delete',WorkdayDelete.as_view(),name="workday_delete"),
   re_path('^(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name="workday_detail"),
]