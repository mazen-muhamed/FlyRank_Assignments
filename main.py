from zipfile import __main__

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def health():
    return jsonify({"Status": "OK"})

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"Message": f"Hello {name}. "})

if __name__ == "__main__":
    app.run(debug=True)