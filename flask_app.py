from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route("/")
def home():
    return render_template("template.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)