# -*- coding: utf-8 -*-
import json


def get_posts_all():
    """
    Функция загружает посты из файла Json
    """
    with open('data/posts.json', 'r', encoding='utf8') as file:
        posts = json.load(file)
        return posts


def get_posts_by_user(user_name=None):
    """
    Функция по значению user_name возвращает все посты связанные с этим user_name
    """
    users = get_posts_all()
    username = []
    for user in users:
        if user_name == user['poster_name']:
            username.append(user)
    return username


def get_comments_by_post_id(post_id):
    """
    Функция по значению post_id) возвращает список всех комментариев, связанных с постом
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
     Функция получает на вход слово и возвращает все посты содержащие это слово
    """
    posts = get_posts_all()
    filter_post = []
    for post in posts:
        if query.lower() in post['content'].lower():
            filter_post.append(post)
    return filter_post


def get_post_by_pk(pk):
    """
    Функция возвращает пост по его индификатору
    """
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post


