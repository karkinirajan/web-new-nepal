import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from news.models import Business, Contact, Newsletter, Post, Sports

CATEGORY_URLS = [
    "national", "covid", "politics", "international", "sports", "entertainment", "lifestyle",
    "blog", "literature", "health", "education", "business", "tech",
]  # fmt: skip


@pytest.fixture
def author(db):
    return User.objects.create_user("editor", "e@example.com", "pw-12345-xyz")


def make_post(author, title="Headline", model=Post):
    return model.objects.create(
        title=title, post_owner="Desk", author=author, address_month_day="Jan 1", text="<p>x</p>"
    )


def test_home_paginates_six_newest_first(client, author):
    for i in range(8):
        make_post(author, f"p{i}")
    res = client.get(reverse("home"))
    assert res.status_code == 200
    assert len(res.context["posts"]) == 6
    assert res.context["posts"][0].title == "p7"
    assert len(client.get(reverse("home") + "?page=2").context["posts"]) == 2


def test_post_detail(client, author):
    p = make_post(author)
    res = client.get(reverse("post-detail", args=[p.pk]))
    assert res.status_code == 200
    assert b"Headline" in res.content


@pytest.mark.parametrize("name", CATEGORY_URLS)
def test_category_pages_render(client, db, name):
    assert client.get(reverse(name)).status_code == 200


def test_category_page_lists_only_its_category(client, author):
    make_post(author, "biz", Business)
    make_post(author, "sport", Sports)
    res = client.get(reverse("business"))
    assert [b.title for b in res.context["business"]] == ["biz"]


def test_create_requires_login(client, db):
    res = client.get(reverse("post-create"))
    assert res.status_code == 302
    assert "login" in res.url


def test_only_author_can_update_or_delete(client, author):
    p = make_post(author)
    other = User.objects.create_user("other", password="pw-12345-xyz")
    client.force_login(other)
    assert client.get(reverse("post-update", args=[p.pk])).status_code == 403
    assert client.post(reverse("post-delete", args=[p.pk])).status_code == 403
    assert Post.objects.filter(pk=p.pk).exists()


def test_author_can_delete(client, author):
    p = make_post(author)
    client.force_login(author)
    assert client.post(reverse("post-delete", args=[p.pk])).status_code == 302
    assert not Post.objects.filter(pk=p.pk).exists()


def test_contact_requires_login(client, db):
    assert client.get(reverse("contact")).status_code == 302


def test_contact_saves_message(client, author):
    client.force_login(author)
    res = client.post(
        reverse("contact"),
        {"name": "A", "email": "a@example.com", "phone": "1", "message": "hi"},
    )
    assert res.status_code == 302
    assert Contact.objects.get().user_id == author.id


def test_subscribe_get_redirects_instead_of_crashing(client, db):
    assert client.get(reverse("subscribe")).status_code == 302


def test_subscribe_anonymous_without_user_id(client, db):
    res = client.post(reverse("subscribe"), {"name": "A", "email": "a@example.com"})
    assert res.status_code == 302
    assert Newsletter.objects.filter(email="a@example.com").count() == 1


def test_subscribe_rejects_duplicate_email(client, db):
    data = {"name": "A", "email": "a@example.com"}
    client.post(reverse("subscribe"), data)
    client.post(reverse("subscribe"), data)
    assert Newsletter.objects.filter(email="a@example.com").count() == 1
