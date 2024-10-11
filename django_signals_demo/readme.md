# Django Signals Synchronous Execution Demo

This project demonstrates that Django signals are executed synchronously by default.

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

## What it demonstrates

- The view function creates a new `MyModel` instance.
- A signal handler is triggered that simulates a time-consuming task (5-second delay).
- The total execution time is displayed, showing that it's over 5 seconds.
- This proves that the signal handler runs synchronously, blocking the main thread.

## Key Files

- `signals_app/models.py`: Contains the `MyModel` and signal handler definition.
- `signals_app/views.py`: Contains the view function that creates the model instance.