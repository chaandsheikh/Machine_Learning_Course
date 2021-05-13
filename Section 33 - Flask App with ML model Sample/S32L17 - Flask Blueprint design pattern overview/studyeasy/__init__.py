from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdf55sd411415a8554a2d1'

from studyeasy.main.routes import main 
from studyeasy.blog.routes import blog

app.register_blueprint(main)
app.register_blueprint(blog)

