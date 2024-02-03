from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "qowijeqiwo"

    from .views import views # импорт переменной
    from .auth import auth

    # регистрация блупринтов
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    return app