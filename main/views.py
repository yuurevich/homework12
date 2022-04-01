from flask import Blueprint, render_template, request
from functions import load_posts, search_posts
import logging

main_blueprint = Blueprint('main_blueprint', __name__)
logging.basicConfig(level=logging.INFO)


@main_blueprint.route('/')
def loader():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    s = request.args.get('s')
    posts = search_posts(s)
    logging.info("Поиск выполнен")
    return render_template('post_list.html', text=s, posts=posts)



