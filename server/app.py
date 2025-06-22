from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.config import Config
from server.models import db
from server.models import user, guest, episode, appearance

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp
    from server.controllers.auth_controller import auth_bp

    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def home():
        return "Welcome to the Late Show API!"

    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error="Not found"), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error="Bad request"), 400

    @app.errorhandler(500)
    def server_error(e):
        return jsonify(error="Server error"), 500

    return app

app = create_app()
