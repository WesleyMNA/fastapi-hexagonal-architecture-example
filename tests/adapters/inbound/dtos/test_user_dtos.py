import pytest
from pydantic import ValidationError

from src.adapters.inbound.dtos import UserRequest, UserPatchRequest, UserResponse


class TestUserCreate:
    def test_user_create_valid(self):
        user = UserRequest(name='John Doe', email='john@example.com')

        assert user.name == 'John Doe'
        assert user.email == 'john@example.com'

    def test_user_create_missing_name(self):
        with pytest.raises(ValidationError):
            UserRequest(email='john@example.com')

    def test_user_create_missing_email(self):
        with pytest.raises(ValidationError):
            UserRequest(name='John Doe')


class TestUserPatch:
    def test_user_patch_empty(self):
        user = UserPatchRequest()

        assert user.name is None
        assert user.email is None

    def test_user_patch_partial_update_name(self):
        user = UserPatchRequest(name='Jane')

        assert user.name == 'Jane'
        assert user.email is None

    def test_user_patch_partial_update_email(self):
        user = UserPatchRequest(email='jane@example.com')

        assert user.name is None
        assert user.email == 'jane@example.com'

    def test_user_patch_full_update(self):
        user = UserPatchRequest(name='Jane', email='jane@example.com')

        assert user.name == 'Jane'
        assert user.email == 'jane@example.com'


class TestUserResponse:
    def test_user_response_valid(self):
        user = UserResponse(id=1, name='John Doe', email='john@example.com')

        assert user.id == 1
        assert user.name == 'John Doe'
        assert user.email == 'john@example.com'

    def test_user_response_invalid_id(self):
        with pytest.raises(ValidationError):
            UserResponse(id='one', name='John Doe', email='john@example.com')
