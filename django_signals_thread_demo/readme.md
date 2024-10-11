# Django Signals Thread Behavior Demo

This project demonstrates that Django signals run in the same thread as the caller by default.

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

1. Navigate to `http://127.0.0.1:8000/create-thread/` in your web browser.
2. Check the console output where the server is running.

## What it demonstrates

- The view function creates a new `ThreadModel` instance.
- Both the view function and the signal handler print their current thread name.
- The output shows that both are running in the same thread.
- This proves that Django signals run in the same thread as the caller by default.

## Key Files

- `thread_app/models.py`: Contains the `ThreadModel` and signal handler definition.
- `thread_app/views.py`: Contains the view function that creates the model instance.