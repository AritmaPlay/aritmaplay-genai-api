from flask import Flask, jsonify
import os
import vertexai
from vertexai.generative_models import GenerativeModel
import re

app = Flask(__name__)

# Inisialisasi Google Cloud Credentials
GOOGLE_CREDENTIALS_FILE = "/secrets/capstone-c242-ps102-592cd9da967c.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS_FILE

# Konfigurasi Google Cloud Project dan Lokasi
PROJECT_ID = "capstone-c242-ps102"
LOCATION = "asia-southeast1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

@app.route('/generate-motivation', methods=['POST'])
def generate_motivation():
    # Prompt tetap yang akan digunakan
    prompt = (
        """Berikan kata-kata motivasi yang unik dan kreatif untuk seseorang yang kalah dalam kuis matematika dengan syarat
    1. Gunakan bahasa santai namun sopan
    2. Hindari kalimat repetitif
    3. Mudah dipahami
    4. Buat dalam 1 kalimat
    5. Hindari penggunaan emoji pada akhir kalimat"""
    )
    
    # Inisialisasi model Gemini
    model = GenerativeModel(model_name="gemini-1.5-flash-002")
    chat = model.start_chat()
    
    try:
        # Kirim prompt ke model dan dapatkan respons
        response = chat.send_message(prompt)
        # Bersihkan karakter newline dan spasi berlebihan
        cleaned_response = response.text.strip()  # Menghapus spasi dan newline di awal/akhir
        cleaned_response = re.sub(r'\s+', ' ', cleaned_response)  # Mengganti spasi berlebihan dengan satu spasi
        return jsonify({"response": cleaned_response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__== '__main__':
    app.run(host='0.0.0.0', port=8080)
