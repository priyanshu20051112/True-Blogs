from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
db = SQLAlchemy()
def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY']='your_secret'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    db.init_app(app)

    from app.routes.auth import auth
    from app.routes.blog import Blog_bp

    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(Blog_bp,url_prefix='/')

    with app.app_context():
        db.create_all()
    return app
    