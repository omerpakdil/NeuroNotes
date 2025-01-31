from flask import jsonify, request
from . import mindmap_bp
from ...utils.firebase_service import FirebaseService
from ...utils.openai_service import OpenAIService

# Service instances
openai_service = OpenAIService()
firebase_service = FirebaseService()

@mindmap_bp.route('/generate', methods=['POST'])
async def generate_mindmap():
    try:
        text = request.json.get('text')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        # Generate mind map with GPT-4
        mindmap_json = await openai_service.generate_mindmap(text)
        return jsonify({'mindmap': mindmap_json}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@mindmap_bp.route('/save', methods=['POST'])
async def save_mindmap():
    try:
        user_id = request.json.get('userId')
        mindmap_data = request.json.get('mindmap')
        
        if not user_id or not mindmap_data:
            return jsonify({'error': 'Missing required fields'}), 400
            
        # Save to Firebase
        mindmap_id = await firebase_service.save_mindmap(user_id, mindmap_data)
        return jsonify({'id': mindmap_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@mindmap_bp.route('/list', methods=['GET'])
async def list_mindmaps():
    try:
        user_id = request.args.get('userId')
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
            
        # Get user's mind maps from Firebase
        mindmaps = await firebase_service.get_user_mindmaps(user_id)
        return jsonify({'mindmaps': mindmaps}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@mindmap_bp.route('/delete/<mindmap_id>', methods=['DELETE'])
async def delete_mindmap(mindmap_id):
    try:
        user_id = request.args.get('userId')
        if not user_id:
            return jsonify({'error': 'User ID is required'}), 400
            
        # Delete mind map from Firebase
        await firebase_service.delete_mindmap(user_id, mindmap_id)
        return jsonify({'message': 'Mind map deleted successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@mindmap_bp.route('/test/save', methods=['POST'])
async def test_save():
    """
    Test endpoint to save data to Firestore
    """
    try:
        test_data = {
            'title': 'Test Mindmap',
            'content': 'This is a test mindmap'
        }
        doc_id = await firebase_service.save_mindmap('test_user', test_data)
        return jsonify({
            'status': 'success',
            'message': 'Test data saved successfully',
            'doc_id': doc_id
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@mindmap_bp.route('/test/list', methods=['GET'])
async def test_list():
    """
    Test endpoint to list data from Firestore
    """
    try:
        mindmaps = await firebase_service.get_user_mindmaps('test_user')
        return jsonify({
            'status': 'success',
            'mindmaps': mindmaps
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@mindmap_bp.route('/test/delete/<mindmap_id>', methods=['DELETE'])
async def test_delete(mindmap_id):
    """
    Test endpoint to delete data from Firestore
    """
    try:
        await firebase_service.delete_mindmap('test_user', mindmap_id)
        return jsonify({
            'status': 'success',
            'message': 'Mindmap deleted successfully'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500 