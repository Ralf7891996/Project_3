import json


def get_posts_all():
    """
    ������� ��������� ����� �� ����� Json
    """
    with open('data/posts.json', 'r', encoding='utf8') as file:
        posts = json.load(file)
        return posts


def get_posts_by_user(user_name=None):
    """
    ������� �� �������� user_name ���������� ��� ����� ��������� � ���� user_name
    """
    users = get_posts_all()
    username = []
    for user in users:
        if user_name == user['poster_name']:
            username.append(user)
    return username


def get_comments_by_post_id(post_id):
    """
    ������� �� �������� post_id) ���������� ������ ���� ������������, ��������� � ������
    """
    with open('data/comments.json', 'r', encoding='utf8') as file:
        comments = json.load(file)
        comments_post = []
        for comment in comments:
            if comment['post_id'] == int(post_id):
                comments_post.append(comment)
        return comments_post


def search_for_posts(query=None):
    """
     ������� �������� �� ���� ����� � ���������� ��� ����� ���������� ��� �����
    """
    posts = get_posts_all()
    filter_post = []
    for post in posts:
        if query.lower() in post['content'].lower():
            filter_post.append(post)
    return filter_post


def get_post_by_pk(pk):
    """
    ������� ���������� ���� �� ��� ������������
    """
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


