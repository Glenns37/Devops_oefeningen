from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Pf1: Basis Experiment Geslaagd!</h1><p>Deze app draait op poort 5051.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)
