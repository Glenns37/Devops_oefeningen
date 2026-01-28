from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulier():
    data = None
    
    # Als het een POST request is (iemand klikte op Verstuur)
    if request.method == 'POST':
        naam = request.form.get('gebruiker')
        bericht = request.form.get('bericht')
        data = {"naam": naam, "msg": bericht}

    return render_template('feedback.html', ontvangen=data)

if __name__ == '__main__':
    # We gebruiken poort 5054 voor Ap4
    app.run(host='0.0.0.0', port=5054)
