from flask import render_template, redirect, url_for, Blueprint
from studyeasy.blog.forms import Register

blog = Blueprint('blog', __name__)

@blog.route('/register', methods=('GET', 'POST'))
def register():
    form = Register()
    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Register', form=form)

@blog.route('/posts')
def posts():
    return render_template('posts.html', title='Posts')


@blog.route('/add_post')
def add_post():
    return render_template('add_post.html', title='Add post')