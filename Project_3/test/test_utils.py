from Project_3.utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, get_post_by_pk, search_for_posts

# Тестим функции из utils
def test_get_posts_all():
    responce = get_posts_all()
    assert isinstance(responce, list)
    for dict in responce:
        assert dict.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_post_by_pk():
    responce = get_post_by_pk(1)
    assert isinstance(responce, dict)
    assert responce.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_posts_by_user():
    responce = get_posts_by_user(1)
    assert isinstance(responce, list)
    for dict in responce:
        assert dict.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_get_comments_by_post_id():
    responce = get_comments_by_post_id(1)
    assert isinstance(responce, list)
    for dict in responce:
        assert dict.keys() == {"post_id", "commenter_name", "comment", "pk"}


def test_search_for_posts():
    responce = search_for_posts()
    assert isinstance(responce, list)
    for dict in responce:
        assert dict.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}