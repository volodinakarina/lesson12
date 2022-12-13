import logging

from flask import Blueprint, render_template, request, current_app

from main.utils import PostsHandler

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    substr = request.args.get('s')
    logging.info(f'Поиск: {substr}')
    posts_handler = PostsHandler(current_app.config['POST_PATH'])
    posts = posts_handler.search_posts(substr)

    return render_template('post_list.html', posts=posts, substr=substr)



