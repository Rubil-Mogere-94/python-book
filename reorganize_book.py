import os
import re

filepath = '/home/solregem/bot/The_Complete_Compendium.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Split the content by the book headers
# The split string was "# Book: "
parts = content.split('# Book: ')

header = parts[0]
book_dict = {}

for p in parts[1:]:
    # The first line is the book name
    first_newline = p.find('\n')
    book_name = p[:first_newline].strip()
    book_content = p[first_newline:].strip()
    book_dict[book_name] = book_content

beginner_content = """# The Complete Journey: Mastering Python from Beginner to Expert

## Introduction
Welcome to the definitive guide to Python. This book is structurally arranged to take you from a complete novice to an architect of distributed, intelligent systems. 

# Part I: The Novice (Beginner Foundations)
Before diving into the virtual machine or asynchronous reactors, you must master the syntax and fundamental structures of Python.

### Chapter 1: The Basics
Python is an interpreted, high-level, dynamically typed language.
*   **Variables and Types**: `x = 5` (int), `y = "Hello"` (str), `z = 3.14` (float), `is_active = True` (bool).
*   **Control Flow**:
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

for i in range(5):
    print(i)
    
while x > 0:
    x -= 1
```

### Chapter 2: Data Structures
Python provides powerful built-in data structures.
*   **Lists**: Ordered, mutable arrays. `my_list = [1, 2, 3]`. Add items with `.append()`.
*   **Tuples**: Ordered, immutable arrays. `my_tuple = (1, 2, 3)`.
*   **Dictionaries**: Key-value stores (hash maps). `my_dict = {"name": "Alice", "age": 30}`.
*   **Sets**: Unordered collections of unique items. `my_set = {1, 2, 3}`.

### Chapter 3: Functions and Scope
Functions are reusable blocks of code.
```python
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"
```
Variables created inside a function are in the *local scope*. Variables created outside are in the *global scope*.

### Chapter 4: Object-Oriented Programming (OOP) Basics
Classes are blueprints for creating objects.
```python
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

# Part II: The Adept (Intermediate Mastery)
Moving beyond the basics to idiomatic, "Pythonic" code.

### Chapter 5: Comprehensions and Generators
*   **List Comprehensions**: A concise way to create lists. `squares = [x**2 for x in range(10)]`.
*   **Generators**: Functions that `yield` values one at a time, saving memory.
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

### Chapter 6: Decorators and Context Managers
*   **Decorators**: Functions that modify the behavior of other functions. Used heavily in frameworks like Flask or FastAPI (e.g., `@app.route("/")`).
*   **Context Managers**: The `with` statement ensures resources are properly acquired and released (e.g., closing files).
```python
with open("file.txt", "r") as f:
    content = f.read()
# f is automatically closed here.
```

### Chapter 7: Error Handling
Catching exceptions prevents your program from crashing abruptly.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This always executes.")
```

---
"""

# Now assemble in the correct order for mastery
# 1. Beginner Content
# 2. Pythonic Singularity (Idiomatic Python, Advanced usage)
# 3. Cpython Codex (Internals, Virtual Machine)
# 4. Atlas Of Autonomy (AI, Distributed, Reactor)
# 5. Omniscience Of Python (Comprehensive overflow)

final_order = [
    "Pythonic Singularity",
    "Cpython Codex",
    "Atlas Of Autonomy",
    "Omniscience Of Python"
]

final_content = beginner_content

# Add a section marker for the Advanced modules
final_content += "\n# Part III: The Expert (Deep Internals and Idiomatic Patterns)\n\n"

for name in final_order:
    if name in book_dict:
        final_content += f"\n\n# Source Book: {name}\n\n"
        final_content += book_dict[name]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Compendium reorganized successfully!")
