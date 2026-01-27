from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        # Check of wachtwoord admin/Cisco123 is
        if request.form['username'] == 'admin' and request.form['password'] == 'Cisco123':
            return f"<h1>Welkom admin!</h1><p>Je bent ingelogd op Pf2.</p>"
        else:
            msg = "Fout wachtwoord, probeer opnieuw."
    return render_template("login.html", msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5052)
