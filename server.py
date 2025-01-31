from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Remplace "TON_TOKEN_HUGGINGFACE" par ton token Hugging Face
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
HEADERS = {"Authorization": "Bearer TON_TOKEN_HUGGINGFACE"}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Message vide"}), 400

    response = requests.post(HUGGINGFACE_API_URL, headers=HEADERS, json={"inputs": user_input})
    
    if response.status_code != 200:
        return jsonify({"error": "Problème API"}), 500

    ai_response = response.json()[0]["generated_text"]
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
