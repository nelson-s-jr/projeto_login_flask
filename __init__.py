from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# inicializando o SQLAlchemy para usarmos depois nos modelos
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        #o user_id é a chave primária da tabela usuário, use-o na query para o usuário
        return User.query.get(int(user_id))

    # blueprint para autenticação de rotas na aplicação
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint para partes de nao-autenticação do app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app