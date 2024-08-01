# survey_app.py
from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Configuração do banco de dados
db_conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST')
)
db_cursor = db_conn.cursor()

@app.route('/survey', methods=['POST'])
def take_survey():
    data = request.json
    if not data or 'response' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    db_cursor.execute("INSERT INTO survey_responses (response) VALUES (%s)", (data['response'],))
    db_conn.commit()
    return jsonify({'message': 'Survey response recorded!'}), 201

@app.route('/results', methods=['GET'])
def get_results():
    db_cursor.execute("SELECT response FROM survey_responses")
    results = db_cursor.fetchall()
    return jsonify([r[0] for r in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
