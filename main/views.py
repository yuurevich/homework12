from flask import Blueprint, render_template, request
from functions import load_posts, search_posts

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def loader():
    return render_template('index.html')


@main_blueprint.route('/search')
def search():
    s = request.args.get('s')
    posts = search_posts(s)
    return render_template('post_list.html', text=s, posts=posts)



