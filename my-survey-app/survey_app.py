from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:123456@Aadbc@10.0.1.176:port/dbtestepq"
db = SQLAlchemy(app)

# Define the table for the database
class SearchRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if query:
        search_request = SearchRequest(query=query)
        db.session.add(search_request)
        db.session.commit()
        return jsonify({"message": "Search request saved successfully"})
    return jsonify({"message": "Invalid request"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
