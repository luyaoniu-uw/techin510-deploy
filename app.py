from flask import Flask, jsonify
import os
import pyodbc

app = Flask(__name__)

@app.route('/')
def home():
    api_key = os.getenv('API_KEY')
    if api_key:
        return jsonify({"message": "API key is set!", "api_key": api_key})
    else:
        return jsonify({"message": "API key is missing!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 