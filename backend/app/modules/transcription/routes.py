from flask import jsonify, request
from . import transcription_bp
from ...utils.openai_service import OpenAIService

# OpenAI service instance
openai_service = OpenAIService()

@transcription_bp.route('/transcribe', methods=['POST'])
async def transcribe_audio():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
            
        audio_file = request.files['file']
        if not audio_file.filename:
            return jsonify({'error': 'No file selected'}), 400
            
        # OpenAI Whisper ile transkripsiyon
        transcript = await openai_service.transcribe_audio(audio_file)
        return jsonify({'transcript': transcript}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@transcription_bp.route('/summarize', methods=['POST'])
async def summarize_text():
    try:
        text = request.json.get('text')
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        # GPT-4 ile özet çıkarma
        summary = await openai_service.generate_summary(text)
        return jsonify({'summary': summary}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400 