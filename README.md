# Django Signals and Custom Python Class Assignment

This project demonstrates various aspects of Django signals behavior and includes a custom Python class implementation. It's divided into four main parts, each addressing a specific question or task.

## Table of Contents
1. [Django Signals Synchronous Execution](#1-django-signals-synchronous-execution)
2. [Django Signals Thread Behavior](#2-django-signals-thread-behavior)
3. [Django Signals Transaction Behavior](#3-django-signals-transaction-behavior)
4. [Custom Rectangle Class](#4-custom-rectangle-class)

## Setup for Django Projects (Parts 1-3)

For each Django project (Parts 1-3), follow these steps:

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install Django:
   ```
   pip install django
   ```

3. Navigate to the specific project directory.

4. Apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server:
   ```
   python manage.py runserver
   ```

## 1. Django Signals Synchronous Execution

This part demonstrates that Django signals are executed synchronously by default.

### Usage
1. Navigate to `http://127.0.0.1:8000/create/` in your web browser.
2. Check the console output where the server is running.

### What it demonstrates
- The view function creates a new `MyModel` instance.
- A signal handler is triggered that simulates a time-consuming task (5-second delay).
- The total execution time is displayed, showing that it's over 5 seconds.
- This proves that the signal handler runs synchronously, blocking the main thread.

### Key Files
- `signals_app/models.py`: Contains the `MyModel` and signal handler definition.
- `signals_app/views.py`: Contains the view function that creates the model instance.

## 2. Django Signals Thread Behavior

This part demonstrates that Django signals run in the same thread as the caller by default.

### Usage
1. Navigate to `http://127.0.0.1:8000/create-thread/` in your web browser.
2. Check the console output where the server is running.

### What it demonstrates
- The view function creates a new `ThreadModel` instance.
- Both the view function and the signal handler print their current thread name.
- The output shows that both are running in the same thread.
- This proves that Django signals run in the same thread as the caller by default.

### Key Files
- `thread_app/models.py`: Contains the `ThreadModel` and signal handler definition.
- `thread_app/views.py`: Contains the view function that creates the model instance.

## 3. Django Signals Transaction Behavior

This part demonstrates that Django signals run in the same database transaction as the caller by default.

### Usage
1. Navigate to `http://127.0.0.1:8000/create/` in your web browser.
2. Check the console output where the server is running.
3. Check the browser response.

### What it demonstrates
- The view function attempts to create a `Parent` object inside a transaction.
- A signal handler is triggered that creates a `Child` object and then raises an exception.
- The exception causes the entire transaction to roll back.
- Neither the `Parent` nor the `Child` object is saved to the database.
- This proves that Django signals run in the same database transaction as the caller by default.

### Key Files
- `transaction_app/models.py`: Contains the `Parent` and `Child` models and signal handler definition.
- `transaction_app/views.py`: Contains the view function that creates the model instances within a transaction.

## 4. Custom Rectangle Class

This part implements a custom Rectangle class in Python with specific iteration behavior.

### Requirements
- Python 3.6 or later

### Usage
1. Create a new Python file (e.g., `rectangle.py`).
2. Copy the Rectangle class implementation into this file.
3. Run the Python script:
   ```
   python rectangle.py
   ```

### What it demonstrates
The Rectangle class meets the following requirements:
1. An instance of the Rectangle class requires `length:int` and `width:int` to be initialized.
2. We can iterate over an instance of the Rectangle class.
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: `{'length': }` followed by the width `{'width': }`.

### Example
```python
rect = Rectangle(5, 3)
for item in rect:
    print(item)
```

Output:
```
{'length': 5}
{'width': 3}
```

### Key Components
- `__init__` method: Initializes the Rectangle with length and width.
- `__iter__` method: Makes the class iterable and yields the length and width in the required format.

This implementation demonstrates object-oriented programming concepts in Python, including class definition, constructor methods, and making a class iterable.

## Conclusion

This project covers various aspects of Django signals behavior and custom Python class implementation. It demonstrates synchronous execution, thread behavior, and transaction behavior of Django signals, as well as the creation of a custom iterable class in Python. Each part provides insights into different aspects of Django and Python programming.
