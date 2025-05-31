from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__)
openai.api_key = "sk-...your-key-here..."

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    prompt = f"""You are a helpful assistant for U.S. visa applications. Focus only on B1/B2 visa.
    Help with:
    - Creating an account
    - Filling the DS-160 form
    - Paying the visa fee
    - Booking an interview
    - Preparing for the interview

    Question: {user_input}
    Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        max_tokens=600
    )

    return jsonify({
        "reply": response['choices'][0]['message']['content']
    })

# This serves the index.html file when you open the site in the browser
@app.route("/")
def serve_homepage():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)