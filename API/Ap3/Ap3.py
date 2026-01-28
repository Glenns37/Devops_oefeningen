from flask import Flask, jsonify

app = Flask(__name__)

# Dit is onze "Database" met dummy data
boeken = [
    {"id": 1, "titel": "DevOps voor Beginners", "auteur": "Jansen"},
    {"id": 2, "titel": "Python API's Bouwen", "auteur": "Peters"}
]

# Route 1: Home (Simpele tekst)
@app.route('/')
def home():
    return "Welkom bij mijn Ap3 API! Ga naar /api/boeken voor de data."

# Route 2: De API (Geeft JSON terug)
@app.route('/api/boeken', methods=['GET'])
def get_boeken():
    # jsonify maakt er nette JSON van (zoals in je slides)
    return jsonify(boeken)

if __name__ == '__main__':
    # We gebruiken poort 5053 voor Ap3
    app.run(host='0.0.0.0', port=5053)
