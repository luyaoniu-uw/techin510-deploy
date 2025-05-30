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

@app.route('/azuresql')
def azuresql_demo():
    server = os.getenv('AZURE_SQL_SERVER')
    database = os.getenv('AZURE_SQL_DATABASE')
    username = os.getenv('AZURE_SQL_USER')
    password = os.getenv('AZURE_SQL_PASSWORD')
    driver = os.getenv('AZURE_SQL_DRIVER', '{ODBC Driver 17 for SQL Server}')
    try:
        conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        with pyodbc.connect(conn_str, timeout=5) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT GETDATE()")
            row = cursor.fetchone()
            return jsonify({"current_time": str(row[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 