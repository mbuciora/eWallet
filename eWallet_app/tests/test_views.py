from django.test import RequestFactory
from ..view import IndexView
from .. import views

class TestIndexView:
    def test_index(self):
        request = RequestFactory().get('/index')
        response = IndexView.IndexView.as_view()(request)
        assert response.status_code == 200, 'IndexView should be callable'

    def test_groupsview(self):
        request = RequestFactory().get('/group')
        response = IndexView.GroupsView.as_view()(request)
        assert response.status_code == 200, 'GroupsView should be callable'

# class TestViews:
#     def test_userchange(self):
#         request = RequestFactory().get('/userchange')
#         response = views.UserChangeList.as_view()(request)
#         assert response.status_code == 200, 'UserChangeList should be callable'
