from flask import Flask
from dotenv import load_dotenv
import os


def create_server():
    load_dotenv() 
    server = Flask(__name__)
    env = os.getenv("APP_ENV", "production")
    
    set_config(server, env)

    print("test secret: " + server.config.get("SECRET"))

    from .routes import main
    server.register_blueprint(main.bp)

    return server
    


def set_config(server, env):
    if env == "development":
        from .config import DevelopmentConfig
        server.config.from_object(DevelopmentConfig)
    elif env == "testing":
        from .config import TestingConfig
        server.config.from_object(TestingConfig)
    else:
        from .config import ProductionConfig
        server.config.from_object(ProductionConfig)
