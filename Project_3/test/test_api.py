from Project_3.main import app


# Тестим эндпоинты
def test_posts():
    """
     Функция проверяет выполнил ли эндпоинт подключение к серверу, возвращает ли он список словарей и содержат ли словари нужные ключи
    """
    responce = app.test_client().get('/api/posts/')
    assert responce.status_code == 200
    assert isinstance(responce.json, list)
    for dict in responce.json:
        assert dict.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_post():
    """
    Функция проверяет выполнил ли эндпоинт подключение к серверу, возвращает ли он словарь и содержат ли словарь нужные ключи
    """
    responce = app.test_client().get('/api/posts/1')
    assert responce.status_code == 200
    assert isinstance(responce.json, dict)
    assert responce.json.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
