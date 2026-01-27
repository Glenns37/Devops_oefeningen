from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/status")
def status():
    return jsonify({
        "service": "Pf3-Eigen-Microservice",
        "status": "active",
        "port": 5053,
        "message": "Dit is een JSON antwoord, geen HTML!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5053)
