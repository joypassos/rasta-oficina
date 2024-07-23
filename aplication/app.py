import cx_Oracle
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração da conexão com o Oracle DB
dsn = cx_Oracle.makedsn(
    os.getenv('ORACLE_HOST', 'localhost'),
    os.getenv('ORACLE_PORT', '1521'),
    service_name=os.getenv('ORACLE_SERVICE_NAME', 'orclpdb1')
)
connection = cx_Oracle.connect(
    user=os.getenv('ORACLE_USER', 'admin'),
    password=os.getenv('ORACLE_PASSWORD', 'password'),
    dsn=dsn
)

@app.route('/create_poll', methods=['POST'])
def create_poll():
    data = request.json
    poll_question = data.get('question')
    poll_options = data.get('options')

    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO polls (question) VALUES (:question)
    """, question=poll_question)
    poll_id = cursor.lastrowid

    for option in poll_options:
        cursor.execute("""
            INSERT INTO poll_options (poll_id, option_text) VALUES (:poll_id, :option_text)
        """, poll_id=poll_id, option_text=option)

    connection.commit()
    return jsonify({'poll_id': poll_id})

@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    poll_id = data.get('poll_id')
    option_id = data.get('option_id')

    cursor = connection.cursor()
    cursor.execute("""
        UPDATE poll_options SET votes = votes + 1 WHERE poll_id = :poll_id AND id = :option_id
    """, poll_id=poll_id, option_id=option_id)
    connection.commit()
    return jsonify({'message': 'Vote counted'})

@app.route('/results/<int:poll_id>', methods=['GET'])
def results(poll_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT option_text, votes FROM poll_options WHERE poll_id = :poll_id
    """, poll_id=poll_id)
    results = cursor.fetchall()
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
