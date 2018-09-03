from django.urls import reverse
import pytest

from crud.views import UserListView, UserUpdate

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
    user.save()
    client.login(username="admin", password="admin123")
    response = client.get(url)
    assert 200 == response.status_code


def test_list_users(rf, user, superuser):
    request = rf.get(reverse("user-list"))
    request.user = superuser
    response = UserListView.as_view()(request)
    assert response.status_code == 200
    assert response.context_data["users"].count() == 1


def test_update_user(rf, user, superuser):
    post_data = {"first_name": "update_name"}
    request = rf.post(reverse("user-update", args=(user.pk,)), data=post_data)
    request.user = superuser
    response = UserUpdate.as_view()(request, pk=user.pk, data=post_data)
    import pdb ; pdb.set_trace()
    assert response.status_code == 200
    assert response.context_data["object"].first_name == post_data["first_name"]
