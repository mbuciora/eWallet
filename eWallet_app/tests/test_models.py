import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestUser:
    def test_user(self):
        obj = mixer.blend('eWallet_app.User')
        assert obj.pk ==1, 'Should create a User instance'

    def test_get_characters(self):
        obj = mixer.blend('eWallet_app.User', username='newUser')
        result = obj.get_characters(4)
        assert result == 'newU', 'Should return first 4 letters'