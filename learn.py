"""
Complete guide to variables in Python.
Run this file directly: python variables_demo.py
"""

# 1. Basic assignment and built-in data types
student_name = "Yacine"          # str (string / text)
age = 21                         # int (integer)
gpa = 3.85                       # float (floating-point number)
is_enrolled = True               # bool (boolean: True or False)
graduation_date = None           # NoneType (represents absence of a value)

print("--- 1. Basic Types ---")
print(f"Name: {student_name} | Type: {type(student_name).__name__}")
print(f"Age: {age} | Type: {type(age).__name__}")
print(f"GPA: {gpa} | Type: {type(gpa).__name__}")
print(f"Enrolled: {is_enrolled} | Type: {type(is_enrolled).__name__}")
print(f"Graduation: {graduation_date} | Type: {type(graduation_date).__name__}")

# 2. Dynamic typing (reassigning a variable to a new value and type)
value = 100
print("\n--- 2. Dynamic Typing ---")
print("Initial:", value, type(value).__name__)

value = "One Hundred"
print("Reassigned to string:", value, type(value).__name__)

value = [100, 200, 300]
print("Reassigned to list:", value, type(value).__name__)

# 3. Constants (convention in UPPER_SNAKE_CASE)
MAX_ATTEMPTS = 3
PI_APPROX = 3.14159

# 4. Multiple assignment and swapping values
a, b, c = 1, 2, 3
print("\n--- 3. Multiple Assignment & Swapping ---")
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")
print(f"c remains:   c={c}")

# 5. Updating variables in place
score = 10
score += 5   # Same as: score = score + 5
score *= 2   # Same as: score = score * 2
print("\n--- 4. In-Place Updates ---")
print("Final score:", score)

# 6. Variable scope (global vs. local)
greeting = "Hello"  # Global variable

def personalize_greeting(person: str) -> str:
    # 'person' and 'message' are local to this function
    message = f"{greeting}, {person}!"
    return message

print("\n--- 5. Scope ---")
print(personalize_greeting("Salma"))
print("Global greeting still:", greeting)