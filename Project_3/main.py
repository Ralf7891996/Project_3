from flask import Flask, render_template, jsonify, request

from Project_3.logs import api_log
from utils import get_posts_all, get_comments_by_post_id, get_posts_by_user, get_post_by_pk, search_for_posts

app = Flask(__name__)


# Сделаем ленту, отображающую все посты
@app.route("/")
def view_posts():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


# Сделаем представление для одного поста
@app.route("/posts/<int:pk>")
def view_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    count_comment = len(comments)
    return render_template('post.html', post=post, comments=comments, count_comment=count_comment)


# Реализуем поиск
@app.route('/search/')
def search_post():
    word = request.args.get('s', '')
    posts = search_for_posts(query=word)
    count_post = len(posts)
    return render_template('search.html', posts=posts, count_post=count_post)


# Реализуем поиск по юзеру
@app.route("/user/<user_name>")
def search_users(user_name):
    posts = get_posts_by_user(user_name=user_name)
    return render_template('user-feed.html', posts=posts)


# Добавляем обработчики ошибок
@app.errorhandler(404)
def not_found(e):
    return render_template('error_404.html')


@app.errorhandler(500)
def server_error(e):
    return render_template('error_500.html')


# сделаем 2 API - эндпоинта
log = api_log.get_logger('api')


@app.route("/api/")
def api_view_posts():
    posts = get_posts_all()
    log.info(f" Запрос: api_view_posts - {len(posts)} ")
    return jsonify(posts)


@app.route("/api/posts/<int:pk>")
def api_view_post(pk):
    post = get_post_by_pk(pk)
    log.info(f"Запрос: api_view_post - {pk} ")
    return jsonify(post)


if __name__ == "__main__":
    app.run(debug=True)
