# ChecklistGenerator

A simple Flask web application to create and manage configurable checklists.

## Setup

Install dependencies with pip:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

The server will start on `http://127.0.0.1:5000/`.

## Features

- Create new checklists with any number of items.
- View and update existing checklists.
- Delete checklists.

Checklists are stored in a local SQLite database `checklists.db`.
