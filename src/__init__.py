from flask import Flask
from src.models.todo import db
from src.routes.todo_routes import todo_bp
import os

def create_app():
    app = Flask(__name__)
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/todos')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(todo_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app 