from flask import Flask, jsonify, request
from models import db, bcrypt, User
import os

app = Flask(__name__)

# Configuration
# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-dev-secret-key')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour in seconds

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({
        "message": "Finance Tracker API",
        "version": "1.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/info')
def api_info():
    return jsonify({
        "project": "Finance Tracker",
        "author": "Remonobasi Uba",
        "year": 2026
    })
    
@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        # Get data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or not data.get('username') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Missing required fields'}), 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists'}), 400
        
        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        # Add to database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'User registered successfully',
            'user': new_user.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Login endpoint - returns JWT token"""
    try:
        # Get data from request
        data = request.get_json()
        
        # Validate required fields
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'error': 'Missing username or password'}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        # Find user in database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists
        if not user:
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Check if password is correct
        if not user.check_password(password):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Create JWT token
        access_token = create_access_token(identity=str(user.id))
        
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get current user's profile - PROTECTED ROUTE"""
    # Get user ID from the token
    current_user_id = get_jwt_identity()
    
    # Get user from database
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'profile': user.to_dict()
    }), 200
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)