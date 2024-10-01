## Variables in Python

Variables are temporary storage spaces used to hold data values, which can change throughout the execution of a program.

- **Naming Rules**:
  - Must start with a **letter** or an **underscore (_)**:
    ```python
    my_variable = 10
    _variable = "test"
    ```
  - Cannot start with a **number**:
    ```python
    1_variable = 10  # ❌ Invalid!
    ```
  - Can only contain **alphanumeric characters** and **underscores** (A-Z, a-z, 0-9, _):
    ```python
    Num_1 = 5  # ✔ Valid!
    ```
  - Variable names are **case-sensitive**:
    ```python
    age = 20
    Age = 30
    AGE = 40
    # All are different variables!
    ```

- A variable name **cannot** be any of the [Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp).

> **Remember:** Variables are the building blocks of any program. Choose meaningful names that reflect their purpose!


## Global vs Local Variables in Python 🌍📍

In Python, **variables have scope**, which determines where they can be accessed or modified. Understanding the difference between **global** and **local** variables is crucial for writing clear, bug-free code.

---

### 🔹 Local Variables:
- **Defined inside a function**.
- Only accessible **within that function**.
- When a variable is created inside a function, it is local and cannot be accessed from outside the function.

```python
def my_function():
    local_var = "I am local!"  # Local variable
    print(local_var)  # This works!

my_function()
print(local_var)  # ❌ Error! 'local_var' is not accessible here.



