# Flask Todo App

A simple Todo application built with Flask and MongoDB.

## Project Structure
    
    flask-todo/
│
├── app.py
├── templates/
│   └── todo_form.html
├── data.json
├── requirements.txt
└── README.md


## Features

- Create todo items with name and description
- Automatic generation of Item ID, UUID, and Hash
- MongoDB integration for data persistence
- Modern UI with Bootstrap

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd flask-todo-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up MongoDB:
- Install MongoDB locally or use a cloud service
- Update the `.env` file with your MongoDB connection string

5. Run the application:
```bash
flask run
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
flask-todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main todo page
└── .env               # Environment variables
```

## API Endpoints

- `GET /api/todos` - Get all todo items
- `POST /submittodoitem` - Create a new todo item
  - Request body: `{ "itemName": "string", "itemDescription": "string" }` 