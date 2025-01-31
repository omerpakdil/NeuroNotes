from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)
    
    # Configure app
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key')
    
    # Register blueprints
    from .modules.auth import auth_bp
    from .modules.mindmap import mindmap_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(mindmap_bp, url_prefix='/api/mindmap')
    
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy'}), 200
    
    return app 