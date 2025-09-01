# 🔍 Searching Algorithms in Python

Welcome to the **Searching Project**!  
This repository demonstrates **various searching algorithms** in Python with proper implementations and tests using **Pytest**.  

If you’re new to **Searching in DSA**, this README will guide you step by step with explanations, diagrams, and examples.

---

# 📘 What is Searching in DSA?

Searching is the process of **finding an element** (key/target) inside a collection (array, list, or graph).  
Different algorithms are optimized for **time complexity**, **data type**, and whether the data is **sorted or unsorted**.

---

# 🚀 Algorithms Covered

We have implemented **10 different searching techniques**:

1. Linear Search  
2. Sentinel Linear Search  
3. Binary Search  
4. Meta Binary Search (One-Sided Binary Search)  
5. Ternary Search  
6. Jump Search  
7. Interpolation Search  
8. Exponential Search  
9. Fibonacci Search  
10. Best First Search (Graph-based, Informed Search)

---

# 📊 Visual Explanations of Algorithms

---

## 1️⃣ Linear Search

- Works on **unsorted arrays**.  
- Checks each element one by one until the target is found.

```
Array: [1, 3, 5, 7, 9]
Target = 7

1 → 3 → 5 → ✅ 7 found
```

⏱ Time Complexity: **O(n)**  
📦 Space Complexity: **O(1)**

---

## 2️⃣ Sentinel Linear Search

- Improved version of Linear Search.  
- Places the target at the **last index temporarily** to avoid repeated comparisons.

```
Array: [1, 3, 5, 7, 9]
Target = 7
Place 7 at the last → scan until found
```

---

## 3️⃣ Binary Search

- Works only on **sorted arrays**.  
- Repeatedly divides the search space into half.  

```
Array: [1, 3, 5, 7, 9, 11]
Target = 7

Step 1: mid=5 → Target > 5 → search right
Step 2: mid=9 → Target < 9 → search left
Step 3: mid=7 ✅ found
```

⏱ Time Complexity: **O(log n)**

---

## 4️⃣ Meta Binary Search (One-Sided)

- Variant of Binary Search using **bit manipulation**.  
- Reduces the number of comparisons.

---

## 5️⃣ Ternary Search

- Divides the array into **three parts** instead of two.  
- Works on sorted arrays.  

```
Array: [1, 3, 5, 7, 9]
Check mid1, mid2
If target in left → search left
Else if target in right → search right
Else search middle
```

---

## 6️⃣ Jump Search

- Works on **sorted arrays**.  
- Jumps `√n` steps at a time, then does a linear search.  

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Step size = √8 ≈ 3

Check 1 → 7 → ✅ found
```

⏱ Time Complexity: **O(√n)**

---

## 7️⃣ Interpolation Search

- Works best on **uniformly distributed sorted arrays**.  
- Uses a **formula to estimate the position**.

```
pos = low + ( (target - arr[low]) * (high - low) / (arr[high] - arr[low]) )
```

---

## 8️⃣ Exponential Search

- Useful for searching in **infinite or unbounded arrays**.  
- First, find range by **doubling index** → then use **binary search**.

---

## 9️⃣ Fibonacci Search

- Similar to Binary Search but uses **Fibonacci numbers** to divide the array.  
- Works well when division using Fibonacci is cheaper.

---

## 🔟 Best First Search (Informed Search)

- Graph-based search algorithm.  
- Uses a **heuristic (estimation function)** to decide which node to explore first.  
- Implemented with a **priority queue (min-heap)**.

```
Graph: 
   A
  / \
 B   C
 |   |
 D   E

Heuristic guides search towards goal faster.
```

⏱ Time Complexity: Depends on heuristic.

---

# 🧪 Running the Tests

We use **Pytest** for testing.

1. Install dependencies:
```bash
pip install pytest
```

2. Run all tests:
```bash
pytest -v
```

3. Run only array-based search tests:
```bash
pytest tests/test_searching.py -v
```

4. Run only graph-based tests:
```bash
pytest tests/test_searching2.py -v
```

---

# 📂 Project Structure

```
Searching/
│
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── sentinel_linear_search.py
│   ├── meta_binary_search.py
│   ├── ternary_search.py
│   ├── jump_search.py
│   ├── interpolation_search.py
│   ├── exponential_search.py
│   ├── fibonacci_search.py
│   └── best_first_search.py
│
├── test_searching.py
└── test_searching2.py
```

---

# 🎯 Conclusion

- Linear and Sentinel Search → **Unsorted arrays**.  
- Binary, Ternary, Jump, Interpolation, Exponential, Fibonacci → **Sorted arrays**.  
- Best First Search → **Graphs with heuristics**.  

✅ This project gives you **hands-on practice** with searching algorithms in Python.  
✅ You also learn how to **test them with Pytest** effectively.  

---


Pytest

Pytest is one of the most popular testing frameworks in Python.
It is simple to use, yet powerful enough to handle complex test cases for small scripts, large projects, and even frameworks like Flask, Django, and FastAPI.

🔑 Key Features of Pytest

Simple Syntax

No need to write long unittest.TestCase classes.

Just create functions starting with test_.

def test_addition():
    assert 2 + 3 == 5


Automatic Test Discovery

Pytest automatically finds files named test_*.py or *_test.py.

Inside them, functions/classes starting with test_ are executed.

Rich Assertions

Just use Python’s assert.

Pytest shows detailed error messages when a test fails.

Example failure output:

E       assert 10 == 20


Fixtures (Setup/Teardown)

Use @pytest.fixture to share setup data across tests.

import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_length(sample_data):
    assert len(sample_data) == 3


Parametrized Tests

Run the same test function with multiple inputs.

@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 5, 7),
    (10, -1, 9),
])
def test_add(a, b, result):
    assert a + b == result


Markers

You can tag tests and run selectively.

@pytest.mark.slow
def test_heavy_task():
    assert sum(range(1000000)) > 0


Run only fast tests:

pytest -m "not slow"


Plugins & Extensions

pytest-cov → Coverage reports

pytest-django, pytest-flask, pytest-asyncio → Framework integration

Integration with CI/CD

Works seamlessly with GitHub Actions, GitLab CI, Jenkins, etc.

⚙️ Running Pytest

Run all tests:

pytest


Run a specific file:

pytest tests/test_searching.py


Run a specific test:

pytest tests/test_searching.py::test_addition


Show logs/prints:

pytest -s

📊 Why Pytest?

Minimal boilerplate code

Human-readable reports

Scales from simple scripts → enterprise projects

Works across Flask, Django, FastAPI, Machine Learning projects, DSA problems

⭐ If you’re learning DSA, this project is a great way to practice both **algorithms + testing skills**.
