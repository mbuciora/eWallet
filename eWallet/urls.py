from django.conf.urls import url
from django.contrib import admin
from eWallet_app import views
from eWallet_app.view import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UserList.as_view()),
    url(r'^listgroup/', views.GroupList.as_view()),
    url(r'^usergroup/', views.UserGroupList.as_view()),
    url(r'^changedetail/', views.ChangeDetailList.as_view()),
    url(r'^gcdetail/', views.GroupChangeList.as_view()),
    url(r'^ucdetail/', views.UserChangeList.as_view()),

    url(r'^$', IndexView.IndexView.as_view(), name='index'),

    url(r'^register/$', IndexView.UserFormView.as_view(), name='register'),

    url(r'^login/$', IndexView.LoginFormView.as_view(), name='login'),

    url(r'^(?P<pk>[0-9]+)/$', IndexView.DetailView.as_view(), name='detail'),

    url(r'change/add/$', IndexView.CreateChange.as_view(), name='change-add'),

    url(r'change/(?P<pk>[0-9]+)/$', IndexView.UpdateChange.as_view(), name='change-update'),

    url(r'change/(?P<pk>[0-9]+)/delete/$', IndexView.DeleteChange.as_view(), name='change-remove'),

    url(r'^balance/$', IndexView.AccountBalance.as_view(), name='balance'),

    url(r'^group/add/$', IndexView.AddGroup.as_view(), name='addgroup'),

    url(r'^group/(?P<pk>[0-9]+)/$', IndexView.GroupView.as_view(), name='group'),

    url(r'^groups/$', IndexView.GroupsView.as_view(), name='groups'),

    url(r'^add-user/$', IndexView.AddUser.as_view(), name='add-user-to-group'),

    url(r'group/(?P<pk>[0-9]+)/$', IndexView.UpdateGroup.as_view(), name='group-update'),

    url(r'group/(?P<pk>[0-9]+)/delete/$', IndexView.DeleteGroup.as_view(), name='group-remove'),
]
