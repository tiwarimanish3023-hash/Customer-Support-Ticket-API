# Customer Support Ticket API

A simple REST API built using Python, Flask and SQLite.

## Features

- Create a support ticket
- Get all tickets
- Get a ticket by ID
- Update a ticket
- Delete a ticket

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- Postman

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tickets | Create a new ticket |
| GET | /tickets | Get all tickets |
| GET | /tickets/<id> | Get ticket by ID |
| PUT | /tickets/<id> | Update a ticket |
| DELETE | /tickets/<id> | Delete a ticket |

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

3. Open:

http://127.0.0.1:5000/

## Database

The project uses SQLite to store customer support tickets.

## Testing

The API was tested using Postman.