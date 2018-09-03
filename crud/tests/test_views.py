from django.urls import reverse
from django.http.response import Http404
import pytest

from crud.views import UserListView, UserUpdate, UserDelete

VIEWS_URL = (
    reverse("user-list"),
    reverse("user-add"),
    reverse("user-update", args=(999999,)),
    reverse("user-delete", args=(999999,)),
)


@pytest.mark.parametrize("url", VIEWS_URL)
def test_login_required(client, url):
    response = client.get(url)
    assert 302 == response.status_code
    assert "/login" in response.url


@pytest.mark.parametrize("url", VIEWS_URL)
def test_ok_views(client, url, user, superuser):
    user.id = 999999
    user.owner = superuser
    user.save()
    client.login(username="admin", password="admin123")
    response = client.get(url)
    assert 200 == response.status_code


def test_list_empty_users(rf, user, superuser):
    request = rf.get(reverse("user-list"))
    request.user = superuser
    response = UserListView.as_view()(request)
    assert response.status_code == 200
    assert response.context_data["users"].count() == 0


def test_list_users(rf, user, superuser):
    user.owner = superuser
    user.save()
    request = rf.get(reverse("user-list"))
    request.user = superuser
    response = UserListView.as_view()(request)
    assert response.status_code == 200
    assert response.context_data["users"].count() == 1


def test_update_other_user(rf, user, superuser):
    post_data = {"first_name": "update_name"}
    request = rf.post(reverse("user-update", args=(user.pk,)), data=post_data)
    request.user = superuser
    with pytest.raises(Http404) as response:
        UserUpdate.as_view()(request, pk=user.pk, data=post_data)

    assert '404' in str(response)


def test_update_user(rf, user, superuser):
    user.owner = superuser
    user.save()

    post_data = {"first_name": "update_name"}
    request = rf.post(reverse("user-update", args=(user.pk,)), data=post_data)
    request.user = superuser
    response = UserUpdate.as_view()(request, pk=user.pk, data=post_data)
    assert response.status_code == 200
    assert response.context_data["object"].first_name == post_data["first_name"]


def test_delete_other_user(rf, user, superuser):
    request = rf.post(reverse("user-delete", args=(user.pk,)))
    request.user = superuser
    with pytest.raises(Http404) as response:
        UserDelete.as_view()(request, pk=user.pk)

    assert '404' in str(response)


def test_delete_user(rf, user, superuser):
    user.owner = superuser
    user.save()

    request = rf.post(reverse("user-update", args=(user.pk,)))
    request.user = superuser
    response = UserDelete.as_view()(request, pk=user.pk)

    assert response.status_code == 302
    assert '/user/' == response.url
