# Flask_tutorial

## Part 1
pip install flask

## Part 3
pip install flask_wtf

pip install email_validator

## Part 4
pip install flask_sqlalchemy
python
>>> from flaskblog import db
>>> db.create_all() '''create db'''
>>> from flaskblog import User, Post
>>> user_1 = User(username='Corey', email='C@demo.com', password='password')
>>> db.session.add(user_1) '''add user_1'''
>>> user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
>>> db.session.add(user_2) '''add user_2'''
>>> db.session.commit()
>>> User.query.all()
[User('Corey', 'C@demo.com', 'default.jpg'), User('JohnDoe', 'jd@demo.com', 'default.jpg')]
>>> User.query.first()
[User('Corey', 'C@demo.com', 'default.jpg')
>>> user = User.query.filter_by(username='Corey').all()
>>> user
[User('Corey', 'C@demo.com', 'default.jpg')
>>> user.id
1
>>> user = User.query.get(1)
>>> user
[User('Corey', 'C@demo.com', 'default.jpg')
>>> post_1 = Post(title='Blog_1', content='First Content!', user_id=user.id)
>>> post_2 = Post(title='Blog_2', content='Second Content!', user_id=user.id)
>>> db.sesion.add(post_1)
>>> db.sesion.add(post_2)
>>> db.session.commit()
>>> user.posts
[Post('Blog 1', '2021-07-08 16:56:12.533764'), Post('Blog 2', '2021-07-08 16:56:12.534451')]
>>> for post in user.posts:
...   print(post.title)
...
Blog 1
Blog 2
>>> post = Post.query.first()
>>> post
Post('Blog 1', '2021-07-08 16:56:12.533764')
>>> post.user_id
1
>>> post.author
User('Corey', 'C@demo.com', 'default.jpg')

## Part 5
In terminal,
python
>>> from flaskblog.models import User, Post
>>> db.create_all()
>>> User.query.all()
[]

## Part 6
pip install flask-bcrypt

pip install flask-login
