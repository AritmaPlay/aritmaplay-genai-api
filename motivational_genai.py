from flask import Flask, jsonify, request
import os
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
import re

app = Flask(__name__)

# Inisialisasi Google Cloud Credentials
GOOGLE_CREDENTIALS_FILE = "/secrets/capstone-c242-ps102-592cd9da967c.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CREDENTIALS_FILE

# Konfigurasi Google Cloud Project dan Lokasi
PROJECT_ID = "capstone-c242-ps102"
LOCATION = "asia-southeast1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/generate-motivation', methods=['POST'])
def generate_motivation():
    total_question = request.form.get("total_question")
    time = request.form.get("time")
    correct_answer = request.form.get("correct_answer")
    user_name = request.form.get("name")
    quiz_mode = request.form.get("mode")

    prompt = f"""
    Kamu adalah asisten pribadi murid sekolah dasar.
    Tugas utamamu adalah membimbing, mengajari, dan memotivasi murid terkait hasil akademik mereka. 
    Sekarang, fokusmu adalah membuat kalimat saran yang menarik, bermanfaat, dan memotivasi berdasarkan hasil kuis matematika yang mereka kerjakan.
    Instruksi :
    1. Analisis hasil kuis berdasarkan:
        - Jumlah soal benar, Waktu pengerjaan, Tingkat kesulitan kuis (berdasarkan mode kuis)
    2. Berikan saran menggunakan kata motivasi maksimal 30 kata:
        - Gunakan bahasa sederhana dan menyenangkan untuk murid SD
        - Sertakan motivasi untuk meningkatkan kemampuan
        - Perhatikan kecepatan pengerjaan dan akurasi murid
    3. Variasikan saran agar unik dan tidak repetitif.

    Murid ini bernama {user_name} 
    dan baru saja mengerjakan {total_question} soal matematika mode {quiz_mode} dengan jumlah soal benar adalah {correct_answer} soal dalam
    waktu pengerjaan {time} detik.
    """
    
    model = GenerativeModel(model_name="gemini-1.5-flash")
    chat = model.start_chat()
    
    try:
        response = chat.send_message(prompt)
        cleaned_response = response.text.strip()
        cleaned_response = re.sub(r'\s+', ' ', cleaned_response)
        json_response = {
            'success': True,
            'message': 'Generated text successfuly',
            'response_code': 200,
            'data': cleaned_response
        }
        return jsonify(json_response), 200
    
    except Exception as e:
        json_response = {
            'success': False,
            'message': str(e),
            'response_code': 500,
            'data': None
        }
        return jsonify(json_response),500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)