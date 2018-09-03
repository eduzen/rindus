import pytest
from crud.models import UserProfile
from crud.tests.factories import UserProfileFactory


@pytest.mark.django_db
def test_user_count():
    assert UserProfile.objects.count() == 0


@pytest.mark.django_db
def test_user_create():
    UserProfileFactory.create()
    assert UserProfile.objects.count() == 1


@pytest.mark.django_db
def test_user_update():
    user = UserProfileFactory.create()
    assert user.first_name
    user.first_name = "modified"
    user.save()
    assert UserProfile.objects.first().first_name == "modified"
