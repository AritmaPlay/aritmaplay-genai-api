from flask import Flask, request, jsonify
import os
import google.auth
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Initialize Flask app
app = Flask(__name__)

# Set Google Application Credentials
GOOGLE_CREDENTIALS_FILE = "/secrets/capstone-c242-ps102-592cd9da967c.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS_FILE

# Authenticate with Google Cloud
credentials, project = google.auth.default()
print(f"Authenticated to project: {project}")

# Initialize Vertex AI
PROJECT_ID = "capstone-c242-ps102"
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Initialize the generative AI model and chat session
model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

def get_chat_response(chat: ChatSession, prompt: str):
    """Berikan kata-kata motivasi untuk anak-anak yang baru saja kalah dalam kuis matematika dalam 1 kalimat saja."""
    response = chat.send_message(prompt)
    return response.text

@app.route('/generate', methods=['POST'])
def generate_response():
    """
    API endpoint to generate AI responses.
    Request JSON: {"prompt": "<your_prompt>"}
    Response JSON: {"response": "<ai_response>"}
    """
    data = request.get_json()

    # Validate the input
    if not data or "prompt" not in data:
        return jsonify({"error": "Invalid input. 'prompt' is required."}), 400

    prompt = data["prompt"]

    try:
        # Get the AI-generated response
        ai_response = get_chat_response(chat, prompt)
        return jsonify({"response": ai_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)