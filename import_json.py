import json

from flaskblog import db
from flaskblog.models import Post

if __name__ == '__main__':
    post_data = json.loads(open('posts.json').read())
    for post in post_data:
        db.session.add(Post(title=post['title'], content=post['content'], user_id=post['user_id']))
    db.session.commit()