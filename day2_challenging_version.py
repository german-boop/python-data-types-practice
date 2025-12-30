
---

### 2️⃣ `day2_challenging_version.py` (refined, readable)

```python
"""
File: day2_challenging_version.py
Description:
    Practice example focused on Python built-in data types,
    explicit type casting, type comparison, and string concatenation.

Python Version: 3.x
"""

# ------------------------
# Variable definitions
# ------------------------
x: int = 3
y: float = 3.12
z: str = "6"
flag1: bool = True
flag2: bool = False

print("Day 2 - Challenging Version")
print("-" * 24)

# ------------------------
# Type inspection
# ------------------------
print(f"Type of x: {type(x)}")
print(f"Type of y: {type(y)}")
print(f"Type of z: {type(z)}")
print(f"Type of flag1: {type(flag1)}")
print(f"Type of flag2: {type(flag2)}")

print("-" * 24)

# ------------------------
# Arithmetic with explicit casting
# ------------------------
sum_xy = x + int(y)        # float -> int
sum_xz = x + int(z)        # str   -> int
bool_sum = flag1 + flag2   # bool behaves like int

print(f"x + int(y) = {sum_xy}")
print(f"x + int(z) = {sum_xz}")
print(f"flag1 + flag2 = {bool_sum}")

print("-" * 24)

# ------------------------
# Type comparison
# ------------------------
print(f"Is type(x) equal to type(y)? {type(x) == type(y)}")
print(f"Is type(flag1) equal to type(flag2)? {type(flag1) == type(flag2)}")
print(f"Is type(z) equal to type(x)? {type(z) == type(x)}")

print("-" * 24)

# ------------------------
# String concatenation
# ------------------------
concat_str = f"{x}{z}{bool_sum}"
print(f"Concatenated string: {concat_str}")
