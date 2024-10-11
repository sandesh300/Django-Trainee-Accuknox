# Custom Rectangle Class

This project implements a custom Rectangle class in Python with specific iteration behavior.

## Requirements

- Python 3.6 or later

## Usage

1. Create a new Python file (e.g., `rectangle.py`).
2. Copy the Rectangle class implementation into this file.
3. Run the Python script:
   ```
   python rectangle.py
   ```

## What it demonstrates

The Rectangle class meets the following requirements:
1. An instance of the Rectangle class requires `length:int` and `width:int` to be initialized.
2. We can iterate over an instance of the Rectangle class.
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: `{'length': }` followed by the width `{'width': }`.

## Example

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

## Key Components

- `__init__` method: Initializes the Rectangle with length and width.
- `__iter__` method: Makes the class iterable and yields the length and width in the required format.

This implementation demonstrates object-oriented programming concepts in Python, including class definition, constructor methods, and making a class iterable.