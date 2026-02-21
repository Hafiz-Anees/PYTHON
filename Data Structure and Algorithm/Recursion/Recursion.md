# 🔁 Recursion in Programming

## 📌 What is Recursion?

**Recursion** is a programming technique where a function **calls itself** to solve a smaller version of the same problem.

In simple words:  
A function breaks a problem into **smaller subproblems of the same type** until it reaches a stopping point.

---

## 🧠 Example: Factorial

Factorial of 5:

```
5! = 5 × 4 × 3 × 2 × 1
```

Recursive definition:

```
factorial(n) = n × factorial(n - 1)
```


# ⭐ Main Important Steps of Recursion

There are **three essential components**:

## 1️⃣ Base Case (Stopping Condition)

- Prevents infinite recursion  
- Stops the function  

Example:

```javascript
if (n === 1) return 1;
```

Without a base case → Stack Overflow Error

---

## 2️⃣ Recursive Case

- The function calls itself  
- Works on a smaller input  

Example:

```javascript
return n * factorial(n - 1);
```

---

## 3️⃣ Progress Toward Base Case

- Each call must move closer to the base case  
- Input must reduce or simplify  

If it does not → infinite recursion

---

# 🔄 How Recursion Works (Call Stack)

Each recursive call is stored in memory (Call Stack).

Example:

```
factorial(5)
  factorial(4)
    factorial(3)
      factorial(2)
        factorial(1)
```

Then it resolves backward:

```
1 → 2 → 6 → 24 → 120
```

---

# 🔄 Recursion vs Iteration

| Recursion | Iteration |
|------------|------------|
| Function calls itself | Uses loops (`for`, `while`) |
| Uses call stack | Uses loop control |
| Cleaner for complex problems | Usually faster |
| Risk of stack overflow | No stack overflow issue |
| More memory usage | Less memory usage |

---

# ⚖️ Which One is Better?

## ✅ Use Recursion When:

- Problem is naturally recursive  
  - Tree traversal  
  - Graph DFS  
  - Divide & Conquer (Merge Sort, Quick Sort)  
  - Backtracking  
- Code readability matters  

## ✅ Use Iteration When:

- Performance is critical  
- Input size is large  
- Problem is simple repetition  
- Memory efficiency is important  

---

# 🎯 Final Advice

- First solve using **recursion** (improves logical thinking)  
- Then try converting it into **iteration**  
- Compare **time complexity** and **space complexity**

This will make you strong in problem solving and DSA 🚀