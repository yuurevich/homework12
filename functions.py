import json
POST_PATH = 'posts.json'


def load_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def search_posts(arg):
    results = [x for x in load_posts() if arg.lower() in x['content'].lower()]
    return results


def uploads_posts(posts):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file)