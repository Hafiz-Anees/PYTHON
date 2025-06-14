## Pracice Questions to master Functions in Python

---

### **Intermediate Level Questions**

1. **Write a function that takes a list of numbers as input and returns a dictionary with keys as "odd" and "even," and values as lists of the odd and even numbers in the input list.**
   - **Example**: `categorize_numbers([1, 2, 3, 4, 5])` should return `{"odd": [1, 3, 5], "even": [2, 4]}`.

2. **Create a function that accepts any number of keyword arguments and returns a list of only those values whose keys contain the letter "a".**
   - **Example**: `filter_kwargs(name="Alice", age=25, country="USA", hobby="reading")` should return `['Alice', 'reading']`.

3. **Write a function that takes two lists and returns a dictionary where the keys are elements from the first list and values are elements from the second list. If one list is longer, use `None` for the missing values.**
   - **Example**: `list_to_dict(['a', 'b', 'c'], [1, 2])` should return `{'a': 1, 'b': 2, 'c': None}`.

4. **Implement a function that accepts a sentence as a parameter and returns a dictionary with each word as the key and its length as the value. Ignore punctuation.**
   - **Example**: `word_lengths("Hello world!")` should return `{"Hello": 5, "world": 5}`.

5. **Write a recursive function that takes a positive integer `n` and returns the `n`th Fibonacci number.**
   - **Example**: `fibonacci(6)` should return `8`.

---

### **Advanced Level Questions**

1. **Create a decorator function `timing_decorator` that times how long a given function takes to execute and prints this time. Then apply this decorator to a function that calculates the sum of the first `n` numbers.**
   - **Example**: Applying `timing_decorator` to a function like `sum_n_numbers(10000)` should output the sum and the time taken.

2. **Write a function that takes a function and a list as input and returns a new list with each element being the result of applying the function to each element of the list. Use this to apply a lambda function that squares each number in the list.**
   - **Example**: `apply_to_all(lambda x: x**2, [1, 2, 3, 4])` should return `[1, 4, 9, 16]`.

3. **Write a function that calculates the Greatest Common Divisor (GCD) of two numbers using recursion and without using the `math` module.**
   - **Example**: `gcd(48, 18)` should return `6`.

4. **Create a higher-order function `compose` that takes two functions as arguments and returns a new function that applies the first function to its input and then the second function to the result.**
   - **Example**: If `f(x) = x + 1` and `g(x) = x * 2`, then `compose(f, g)(5)` should return `12` (since `g(f(5))` is `12`).

5. **Write a function `memoized_fibonacci` that calculates Fibonacci numbers but uses memoization (caching) to optimize performance, especially for larger values.**
   - **Example**: `memoized_fibonacci(100)` should return the 100th Fibonacci number efficiently. 

---
