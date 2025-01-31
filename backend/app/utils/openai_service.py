import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenAIService:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        if not openai.api_key:
            raise ValueError("OpenAI API key is not set in environment variables")

    async def transcribe_audio(self, audio_file):
        """
        Transcribes audio file to text
        """
        try:
            transcript = await openai.Audio.transcribe("whisper-1", audio_file)
            return transcript.text
        except Exception as e:
            print(f"Error in transcription: {str(e)}")
            raise

    async def generate_summary(self, text):
        """
        Generates a summary of the text
        """
        try:
            response = await openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that creates lecture summaries. "
                     "Summarize the given text focusing on key points and important concepts."},
                    {"role": "user", "content": text}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in summarization: {str(e)}")
            raise

    async def generate_mindmap(self, text):
        """
        Generates a mind map JSON from text
        """
        try:
            response = await openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that creates mind maps. "
                     "Analyze the given text and create a hierarchical mind map structure. "
                     "The output should be in the following JSON format:\n"
                     "{\n"
                     "  'center': {'id': '1', 'text': 'Main Topic'},\n"
                     "  'branches': [\n"
                     "    {'id': '2', 'text': 'Subtopic 1', 'parentId': '1',\n"
                     "     'children': [{'id': '3', 'text': 'Detail 1', 'parentId': '2'}]}\n"
                     "  ]\n"
                     "}"},
                    {"role": "user", "content": text}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in mind map generation: {str(e)}")
            raise 