Here are 10 advanced-level questions on Python lists to help deepen your understanding of list operations, manipulation, and advanced concepts:

### 1. List Comprehensions with Conditional Logic
Create a list comprehension that takes a list of integers and returns a new list where each element is squared if it's even, and cubed if it's odd.  
For example, given the list `[1, 2, 3, 4, 5]`, the output should be `[1, 4, 27, 16, 125]`.

### 2. Flatten a Nested List
Write a function that takes a nested list (a list of lists) and returns a flattened version of it (a single list with all elements).
For example, given the list `[[1, 2, 3], [4, 5], [6]]`, the output should be `[1, 2, 3, 4, 5, 6]`.

### 3. Find the Most Frequent Element
Write a function that finds the most frequently occurring element in a list. If there is a tie, return any one of the most frequent elements.  
For example, given the list `[1, 2, 2, 3, 3, 3, 4, 4]`, the output should be `3`.

### 4. Rotate List Elements
Write a function to "rotate" a list by `k` positions. The function should take two arguments: the list and the integer `k`, which determines how many positions the list should be rotated.  
For example, given the list `[1, 2, 3, 4, 5]` and `k = 2`, the output should be `[4, 5, 1, 2, 3]`.

### 5. Find Pairs with a Given Sum
Write a function that takes a list of integers and a target integer. The function should return all unique pairs of numbers in the list that sum up to the target.  
For example, given the list `[1, 2, 3, 4, 5]` and target `5`, the output should be `[(1, 4), (2, 3)]`.

### 6. Remove Duplicates in Place
Write a function that removes duplicates from a list in place, without using any additional data structures (like sets). The order of elements should be preserved.  
For example, given the list `[1, 2, 2, 3, 4, 4, 5]`, the output should modify the list to `[1, 2, 3, 4, 5]`.

### 7. Group List Elements by a Condition
Write a function that groups the elements of a list into two separate lists based on a condition. For example, group the list by even and odd numbers. The function should return a tuple of two lists: one with even numbers and one with odd numbers.  
For example, given the list `[1, 2, 3, 4, 5, 6]`, the output should be `([2, 4, 6], [1, 3, 5])`.

### 8. Find the Kth Largest Element
Write a function to find the `k`th largest element in a list without sorting the list. You can assume that `k` is always valid and within the range of the list's length.  
For example, given the list `[3, 1, 5, 6, 2, 4]` and `k = 2`, the output should be `5`.

### 9. Spiral Traverse a 2D List
Write a function that takes a 2D list (matrix) and returns a list containing all the elements of the matrix in spiral order (clockwise from the top-left corner).  
For example, given the matrix:
```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
The output should be `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

### 10. Generate All Possible Sublists
Write a function that generates all possible contiguous sublists of a list.  
For example, given the list `[1, 2, 3]`, the output should be `[[1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]`.
