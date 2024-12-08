
# Motivation Generator API

This API aims to generate motivational messages for elementary school students based on their math quiz performance. By utilizing Google Cloud's Vertex AI and Flash's `Gemini 1.5 generative model', this API will provide feedback that is concise and personalized.

---

## Features

- Generate short, motivational messages based on quiz results.
- Feedback is tailored to performance metrics, including accuracy, speed, and quiz difficulty.

---

## Prerequisites

1. **Python 3.9+**
2. **Google Cloud Project**:
   - Vertex AI API enabled.
   - A service account key with proper permissions for Vertex AI.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AritmaPlay/aritmaplay-genai-api.git
   cd aritmaplay-genai-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Google Cloud credentials:
   - Place your service account key JSON file in the project directory.
   - Update the file path in the `GOOGLE_CREDENTIALS_FILE` variable within the code.

---

## Configuration

Update the following variables in the code to match your Google Cloud setup:

```python
GOOGLE_CREDENTIALS_FILE = "/path/to/your/credentials.json"
PROJECT_ID = "your-project-id"
LOCATION = "your-region"
```

---

## API Endpoint

### **Generate Motivational Message**

- **Endpoint**: `/generate-motivation`
- **Method**: `POST`
- **Parameters** (as form data):
  - `name`: (string) Student's name.
  - `total_question`: (integer) Total number of questions in the quiz.
  - `correct_answer`: (integer) Number of correct answers.
  - `time`: (integer) Time taken to complete the quiz (in seconds).
  - `mode`: (string) Quiz difficulty mode (e.g., "Penambahan", "Pengurangan", "Perkalian", "Pembagian").

#### Example Request

```bash
curl -X POST http://localhost:8080/generate-motivation \
    -d "name=Dimas" \
    -d "total_question=10" \
    -d "correct_answer=5" \
    -d "time=100" \
    -d "mode=Penambahan"
```

#### Example Response

**Success:**
```json
{
    "success": true,
    "message": "Generated text successfully",
    "response_code": 200,
    "data": "Dimas, hebat! Kamu sudah setengah jalan! Ayo tingkatkan kecepatan dan ketelitianmu!"
}
```

**Failure:**
```json
{
    "success": false,
    "message": "Error details",
    "response_code": 500,
    "data": null
}
```

---

## Running the Application

1. Start the server:
   ```bash
   python motivational_genai.py
   ```

2. Access the API at:
   ```
   http://localhost:8080
   ```

---

## Notes

- The application uses the `Gemini 1.5 Flash` model from Vertex AI.
- Ensure your Google Cloud service account has access to Vertex AI with appropriate permissions.
- Securely handle your Google Cloud credentials, especially in production.

---
