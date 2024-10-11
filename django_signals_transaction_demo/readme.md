# Django Signals Transaction Behavior Demo

This project demonstrates that Django signals run in the same database transaction as the caller by default.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install Django:
   ```
   pip install django
   ```

3. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to `http://127.0.0.1:8000/create/` in your web browser.
2. Check the console output where the server is running.
3. Check the browser response.

## What it demonstrates

- The view function attempts to create a `Parent` object inside a transaction.
- A signal handler is triggered that creates a `Child` object and then raises an exception.
- The exception causes the entire transaction to roll back.
- Neither the `Parent` nor the `Child` object is saved to the database.
- This proves that Django signals run in the same database transaction as the caller by default.

## Key Files

- `transaction_app/models.py`: Contains the `Parent` and `Child` models and signal handler definition.
- `transaction_app/views.py`: Contains the view function that creates the model instances within a transaction.