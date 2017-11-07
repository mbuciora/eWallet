from django.conf.urls import url
from django.contrib import admin
from eWallet_app import views
from eWallet_app.view import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UserList.as_view()),
    url(r'^groups/', views.GroupList.as_view()),
    url(r'^usergroup/', views.UserGroupList.as_view()),
    url(r'^changedetail/', views.ChangeDetailList.as_view()),
    url(r'^gcdetail/', views.GroupChangeList.as_view()),
    url(r'^ucdetail/', views.UserChangeList.as_view()),

    url(r'^$', IndexView.index, name='index'),
    url(r'^(?P<change_detail_id>[0-9]+)/$', IndexView.detail, name='detail'),

]