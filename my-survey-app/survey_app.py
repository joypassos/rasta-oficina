from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname='dbtestepq',
        user='admin',
        password='123456@Aadbc',
        host='10.0.1.176'
    )
    return conn

@app.route('/survey', methods=['POST'])
def create_survey():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO surveys (question) VALUES (%s)', (data['question'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'survey created'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
