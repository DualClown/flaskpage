from flask import Flask, render_template
import datetime
app = Flask(__name__)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title': 'HOLA!',
        'time': timeString
    }
    return render_template('main.html', **templateData)


if __name__ == "__main__":
    app.run(host='aqui va tu ip', port=80, debug=True)
