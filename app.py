from flask import Flask, jsonify, request
from database import create_table, get_db_connection

app = Flask(__name__)
create_table()

@app.route("/")
def home():
    return jsonify({"message": "Customer Support Ticket API is running!"})
@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    status = data.get("status")
    tags = data.get("tags")
    connection = get_db_connection()
    connection.execute(
        """INSERT INTO tickets (title, description, status, tags, created_at)
        VALUES (?, ?, ?, ?, datetime('now'))""",
        (title, description, status, tags))
    connection.commit()
    connection.close()
    return jsonify({"message": "Ticket created successfully!"}),201

@app.route("/tickets", methods=["GET"])
def get_tickets():
    connection = get_db_connection()
    tickets = connection.execute("SELECT * FROM tickets").fetchall()
    connection.close()

    return jsonify([dict(ticket) for ticket in tickets])

@app.route("/tickets/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    connection = get_db_connection()
    ticket = connection.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,)).fetchone()
    connection.close()

    if ticket is None:
        return jsonify({"error": "Ticket not found"}), 404

    return jsonify(dict(ticket))

@app.route("/tickets/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    data = request.get_json()
    status = data.get("status")
    tags = data.get("tags")

    connection = get_db_connection()
    connection.execute(
        """UPDATE tickets SET status = ?, tags = ?
        WHERE id = ?""",
        (status, tags, ticket_id))
    connection.commit()
    connection.close()

    return jsonify({"message": "Ticket updated successfully!"})


@app.route("/tickets/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Ticket deleted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)