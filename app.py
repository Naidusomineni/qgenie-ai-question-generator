from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "QGenie AI Question Generator Running"})

@app.route("/generate")
def generate():
    return jsonify({
        "questions": [
            "What is Machine Learning?",
            "Explain supervised learning.",
            "What is Generative AI?"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
