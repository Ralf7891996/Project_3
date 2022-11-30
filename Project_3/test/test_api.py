from Project_3.main import app


# ������ ���������
def test_posts():
    """
     ������� ��������� �������� �� �������� ����������� � �������, ���������� �� �� ������ �������� � �������� �� ������� ������ �����
    """
    responce = app.test_client().get('/api/posts/')
    assert responce.status_code == 200
    assert isinstance(responce.json, list)
    for dict in responce.json:
        assert dict.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_post():
    """
    ������� ��������� �������� �� �������� ����������� � �������, ���������� �� �� ������� � �������� �� ������� ������ �����
    """
    responce = app.test_client().get('/api/posts/1')
    assert responce.status_code == 200
    assert isinstance(responce.json, dict)
    assert responce.json.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
