import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from users.models import Profile

REGISTER = {
    "first_name": "A",
    "last_name": "B",
    "username": "alice",
    "email": "alice@example.com",
    "password": "pw-12345-xyz",
    "password2": "pw-12345-xyz",
}


@pytest.fixture
def user(db):
    return User.objects.create_user("bob", "bob@example.com", "pw-12345-xyz")


def test_profile_created_by_signal(user):
    assert Profile.objects.filter(user=user).exists()


def test_register_creates_user(client, db):
    res = client.post(reverse("register"), REGISTER)
    assert res.url == reverse("login")
    assert User.objects.filter(username="alice").exists()


def test_register_rejects_mismatch_and_duplicates(client, user):
    client.post(reverse("register"), {**REGISTER, "password2": "x"})
    client.post(reverse("register"), {**REGISTER, "username": "bob"})
    client.post(reverse("register"), {**REGISTER, "email": "bob@example.com"})
    assert not User.objects.filter(username="alice").exists()


def test_login_success_and_failure(client, user):
    bad = client.post(reverse("login"), {"username": "bob", "password": "nope"})
    assert bad.url == reverse("login")
    ok = client.post(reverse("login"), {"username": "bob", "password": "pw-12345-xyz"})
    assert ok.url == reverse("profile")


def test_logout_post_clears_session_and_get_shows_confirmation(client, user):
    client.force_login(user)
    assert client.get(reverse("logout")).status_code == 200
    assert "_auth_user_id" in client.session
    assert client.post(reverse("logout")).status_code == 302
    assert "_auth_user_id" not in client.session


def test_profile_requires_login(client, db):
    assert client.get(reverse("profile")).status_code == 302


def test_profile_update(client, user):
    client.force_login(user)
    res = client.post(reverse("profile"), {"username": "bob", "email": "new@example.com"})
    user.refresh_from_db()
    assert res.status_code == 302
    assert user.email == "new@example.com"
