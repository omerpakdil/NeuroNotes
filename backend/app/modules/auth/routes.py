from flask import jsonify, request
from . import auth_bp
from ...utils.firebase_service import FirebaseService

# Firebase service instance
firebase_service = FirebaseService()

@auth_bp.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    """
    return jsonify({
        'status': 'healthy',
        'firebase': 'connected' if firebase_service._initialized else 'not connected'
    })

@auth_bp.route('/sign-in-with-apple', methods=['POST'])
async def sign_in_with_apple():
    try:
        id_token = request.json.get('idToken')
        if not id_token:
            return jsonify({'error': 'No ID token provided'}), 400
            
        # Verify Apple ID token and create Firebase custom token
        decoded_token = await firebase_service.verify_token(id_token)
        return jsonify({
            'uid': decoded_token['uid'],
            'email': decoded_token.get('email'),
            'isNewUser': decoded_token.get('isNewUser', False)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/verify-token', methods=['POST'])
async def verify_token():
    try:
        token = request.json.get('token')
        if not token:
            return jsonify({'error': 'No token provided'}), 400
            
        # Firebase token verification
        decoded_token = await firebase_service.verify_token(token)
        return jsonify({'uid': decoded_token['uid']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401 