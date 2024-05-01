from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))


def create_app(test_config=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URI", "postgresql://postgres:post@localhost/umuzi_computers"
    )
    app.app_context().push()
    if test_config == True:
        app.config.from_mapping(TESTING=True, SQLALCHEMY_DATABASE_URI="sqlite://")
        
    from src.models import db

    db.init_app(app)
    db.create_all()
    
    from src import routes

    app.register_blueprint(routes.app_blueprint)

    return app