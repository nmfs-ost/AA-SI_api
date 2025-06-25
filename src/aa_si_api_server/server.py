import signal
from flask import Flask
from dotenv import load_dotenv
import os
from aa_si_api_server.routes.main import bp
# import aalibrary

# Entrypoint for running server
def main():
    try:
        server = create_server()
        server.run(
            host="localhost",
            port=3000,
            use_debugger=False,
            debug=server.config.get("DEBUG"),
            use_reloader=server.config.get("USE_RELOADER"),
        )
    except KeyboardInterrupt:
        print("\nServer stopped by Ctrl+C")


# Create Flask server and use environment variables to set configuration
def create_server():
    load_dotenv()
    server = Flask(__name__)
    env = os.getenv("APP_ENV", "production")
    set_config(server, env)
    print("new test secret: " + server.config.get("SECRET"))
    server.register_blueprint(bp)
    return server


# Load configuration from config file
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


if __name__ == "__main__":
    main()
