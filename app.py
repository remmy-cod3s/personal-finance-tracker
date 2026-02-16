from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Finance Tracker API",
        "version": "1.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/info")
def api_info():  # Changed name to avoid confusion
    return jsonify({
        "project": "Finance Tracker",
        "author": "Remonobasi Uba",
        "year": 2026
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
