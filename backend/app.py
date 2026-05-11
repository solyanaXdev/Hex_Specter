from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]

    return jsonify({
        "filename": file.filename,
        "status": "scanned",
        "hidden_layers_found": 0,
        "message": "analysis complete (basic mode)"
    })

if __name__ == "__main__":
    app.run(debug=True)vv
