from flask import Blueprint, render_template, request
from functions import load_posts, uploads_posts
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__)
logging.basicConfig(level=logging.INFO)


@loader_blueprint.route('/form/')
def post():
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['POST'])
def upload():
    try:
        file = request.files.get('picture')
        filename = file.filename
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'uploads/images/{filename}',
            'content': content
        })
        uploads_posts(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split(".")[-1] not in ["jpeg", "png"]:
            logging.info('Загруженный файл - не картинка')
            return "<h1>Загруженный файл - не картинка</h1>"
    except FileNotFoundError:
        logging.error("Файл не найден")
        return "<h1>Файл не найден</h1>"
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)