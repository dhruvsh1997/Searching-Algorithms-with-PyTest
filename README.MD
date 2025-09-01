# 🔍 Searching Algorithms with PyTest

A comprehensive implementation of various searching algorithms in Python with extensive testing using PyTest. This project demonstrates how to implement, test, and validate different searching techniques with proper software engineering practices.

## 📚 Table of Contents

- [PyTest Tutorial](#-pytest-tutorial)
- [Searching Algorithms Explained](#-searching-algorithms-explained)
- [Project Structure](#-project-structure)
- [Code Analysis](#-code-analysis)
- [Running the Tests](#-running-the-tests)
- [Docker Setup](#-docker-setup)
- [Contributing](#-contributing)

## 🧪 PyTest Tutorial

### What is PyTest?

PyTest is a powerful Python testing framework that makes it easy to write simple and scalable test cases. It's the most popular testing framework in the Python ecosystem due to its simplicity and powerful features.

### Key Features of PyTest

- **Simple syntax**: No need for complex boilerplate code
- **Automatic test discovery**: Finds and runs tests automatically
- **Parametrized testing**: Run the same test with different inputs
- **Fixtures**: Setup and teardown for tests
- **Rich plugin ecosystem**: Extensive customization options

### Basic PyTest Structure

```python
# test_example.py
import pytest

def add(a, b):
    return a + b

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

### Essential PyTest Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_searching.py

# Run tests matching pattern
pytest -k "binary"

# Show test coverage
pytest --cov=Search_Algo

# Generate HTML coverage report
pytest --cov=Search_Algo --cov-report=html
```

### PyTest Markers

```python
@pytest.mark.parametrize  # Run test with multiple parameters
@pytest.mark.skip         # Skip this test
@pytest.mark.xfail        # Expected to fail
@pytest.mark.slow         # Custom marker for slow tests
```

## 🔍 Searching Algorithms Explained

### 1. Linear Search

**Concept**: Check each element one by one until target is found.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 7

Step 1: Check index 0 → 1 ≠ 7
Step 2: Check index 1 → 3 ≠ 7  
Step 3: Check index 2 → 5 ≠ 7
Step 4: Check index 3 → 7 = 7 ✓ Found!
```

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Unsorted arrays, small datasets

### 2. Binary Search

**Concept**: Divide and conquer on sorted arrays by comparing with middle element.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 7

Step 1: mid = 4, arr[4] = 9 > 7, search left half
Step 2: mid = 1, arr[1] = 3 < 7, search right half  
Step 3: mid = 3, arr[3] = 7 = 7 ✓ Found!
```

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Use Case**: Sorted arrays, large datasets

### 3. Jump Search

**Concept**: Jump ahead by fixed steps, then linear search in the identified block.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 11
Jump size: √8 = 2

Step 1: Jump to index 2 → arr[2] = 5 < 11
Step 2: Jump to index 4 → arr[4] = 9 < 11  
Step 3: Jump to index 6 → arr[6] = 13 > 11
Step 4: Linear search in block [4-6] → Found at index 5
```

- **Time Complexity**: O(√n)
- **Space Complexity**: O(1)
- **Use Case**: Large sorted arrays where binary search is costly

### 4. Interpolation Search

**Concept**: Estimate position using value distribution (works best with uniformly distributed data).

```
Formula: pos = low + [(target - arr[low]) / (arr[high] - arr[low])] * (high - low)
```

- **Time Complexity**: O(log log n) for uniform distribution, O(n) worst case
- **Space Complexity**: O(1)
- **Use Case**: Uniformly distributed sorted data

### 5. Exponential Search

**Concept**: Find range where element exists by exponentially increasing bounds, then binary search.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
Target: 15

Step 1: Check index 1 → arr[1] = 3 < 15
Step 2: Check index 2 → arr[2] = 5 < 15
Step 3: Check index 4 → arr[4] = 9 < 15
Step 4: Check index 8 → arr[8] = 17 > 15
Step 5: Binary search in range [4, 8] → Found at index 7
```

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Use Case**: Unbounded or infinite sorted arrays

### 6. Fibonacci Search

**Concept**: Use Fibonacci numbers to divide the array into unequal parts.

```
Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21...
Uses golden ratio properties for optimal division
```

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Use Case**: When division operation is costly

### 7. Ternary Search

**Concept**: Divide array into three parts instead of two (like binary search).

```
Array: [1, 3, 5, 7, 9, 11, 13, 15]
Target: 11

Step 1: mid1 = 2, mid2 = 5
        arr[2] = 5 < 11, arr[5] = 11 = 11 ✓ Found!
```

- **Time Complexity**: O(log₃ n)
- **Space Complexity**: O(1)
- **Use Case**: Theoretical interest, rarely used in practice

### 8. Meta Binary Search

**Concept**: Binary search using bit manipulation without division.

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Use Case**: Systems where division is expensive

### 9. Sentinel Linear Search

**Concept**: Linear search with a sentinel value to avoid boundary checks.

```
Array: [1, 3, 5, 7, 9]
Target: 5

Step 1: Set last element as sentinel (target)
Step 2: Search without boundary checks
Step 3: Restore original last element
```

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Optimization of linear search

### 10. Best First Search

**Concept**: Graph search algorithm using heuristic function to guide search.

```
Graph visualization:
    A(h=3)
   /     \
B(h=2)   C(h=1)
  |        |
D(h=0)   E(h=0)

Search for D from A:
1. Start at A, add to priority queue with heuristic value
2. Pop node with lowest heuristic (best first)
3. Add neighbors to queue
4. Repeat until goal found
```

- **Time Complexity**: O(b^m) where b is branching factor, m is depth
- **Space Complexity**: O(b^m)
- **Use Case**: AI pathfinding, game development, route planning

## 📁 Project Structure

```
SearchingAlgoDSAPytest/
├── envSearchAlgo/              # Virtual environment
├── Search_Algo/                # Algorithm implementations
│   ├── __init__.py
│   ├── best_first_search.py
│   ├── binary_search.py
│   ├── exponential_search.py
│   ├── fibonacci_search.py
│   ├── interpolation_search.py
│   ├── jump_search.py
│   ├── linear_search.py
│   ├── meta_binary_search.py
│   ├── sentinel_linear_search.py
│   └── ternary_search.py
├── test_searching.py           # Main test suite
├── test_searching2.py          # Best first search tests
├── Dockerfile                  # Docker configuration
├── .gitignore                  # Git ignore rules
├── .dockerignore              # Docker ignore rules
├── requirements.txt           # Python dependencies
├── pytest.ini                # PyTest configuration
└── README.md                  # This file
```

## 🔬 Code Analysis

### How PyTest is Utilized

#### 1. Parametrized Testing (`test_searching.py`)

The main test file uses `@pytest.mark.parametrize` to test multiple algorithms with the same test cases:

```python
@pytest.mark.parametrize("func", [
    linear_search,
    binary_search,
    sentinel_linear_search,
    meta_binary_search,
    ternary_search,
    jump_search,
    interpolation_search
])
def test_search_algorithms(func):
    # Test positive cases
    assert func(arr, 7) == arr.index(7)
    assert func(arr, 15) == arr.index(15)
    assert func(arr, 1) == arr.index(1)
    
    # Test negative case
    assert func(arr, 100) == -1
```

**Benefits**:
- Tests all algorithms with identical test cases
- Ensures consistency across implementations
- Easy to add new algorithms
- Reduces code duplication

#### 2. Specialized Testing (`test_searching2.py`)

Best First Search requires different test setup (graph + heuristic):

```python
def test_best_first_search_found():
    graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
    heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0, 'E': 0}
    
    assert best_first_search(graph, 'A', 'D', heuristic) is True
```

### Algorithm Implementation Analysis

#### Array-based Algorithms
All array-based algorithms follow similar patterns:
- **Input validation**: Handle edge cases
- **Boundary management**: Proper index handling
- **Return conventions**: Index if found, -1 if not found

#### Graph-based Algorithms
Best First Search demonstrates:
- **Priority queue usage**: Using heapq for efficient priority management
- **Visited set**: Preventing cycles
- **Heuristic guidance**: Using domain knowledge to guide search

## 🚀 Running the Tests

### Prerequisites

```bash
# Install Python 3.8+
python --version

# Create virtual environment
python -m venv envSearchAlgo

# Activate virtual environment
# On Windows
envSearchAlgo\Scripts\activate
# On macOS/Linux
source envSearchAlgo/bin/activate

# Install dependencies
pip install pytest pytest-cov
```

### Test Commands

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_searching.py

# Run with coverage report
pytest --cov=Search_Algo

# Generate HTML coverage report
pytest --cov=Search_Algo --cov-report=html

# Run tests in parallel (if pytest-xdist installed)
pytest -n auto
```

### Expected Output

```
$ pytest -v

test_searching.py::test_search_algorithms[linear_search] PASSED
test_searching.py::test_search_algorithms[binary_search] PASSED
test_searching.py::test_search_algorithms[sentinel_linear_search] PASSED
test_searching.py::test_search_algorithms[meta_binary_search] PASSED
test_searching.py::test_search_algorithms[ternary_search] PASSED
test_searching.py::test_search_algorithms[jump_search] PASSED
test_searching.py::test_search_algorithms[interpolation_search] PASSED
test_searching2.py::test_best_first_search_found PASSED
test_searching2.py::test_best_first_search_not_found PASSED

========== 9 passed in 0.03s ==========
```

## 🐳 Docker Setup

### Build and Run

```bash
# Build Docker image
docker build -t searching-algo-pytest .

# Run tests in container
docker run --rm searching-algo-pytest

# Run interactive container
docker run -it --rm searching-algo-pytest /bin/bash

# Run with volume mount for development
docker run --rm -v $(pwd):/app searching-algo-pytest
```

## 🔄 CI/CD Pipeline

The project includes GitHub Actions workflow for:
- **Automated testing**: Run tests on multiple Python versions
- **Code coverage**: Generate and upload coverage reports
- **Docker testing**: Ensure Docker build works
- **Dependency checking**: Security vulnerability scanning

## 📊 Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Best Use Case |
|-----------|----------------|------------------|---------------|
| Linear Search | O(n) | O(1) | Small/unsorted arrays |
| Binary Search | O(log n) | O(1) | Large sorted arrays |
| Jump Search | O(√n) | O(1) | Large arrays, costly comparisons |
| Interpolation Search | O(log log n) | O(1) | Uniformly distributed data |
| Exponential Search | O(log n) | O(1) | Unbounded/infinite arrays |
| Fibonacci Search | O(log n) | O(1) | Division is expensive |
| Ternary Search | O(log₃ n) | O(1) | Theoretical interest |
| Meta Binary Search | O(log n) | O(1) | Bit manipulation optimization |
| Sentinel Linear Search | O(n) | O(1) | Optimized linear search |
| Best First Search | O(b^m) | O(b^m) | Graph pathfinding |

## 🎯 Learning Objectives

After working through this project, you will understand:

1. **PyTest Fundamentals**:
   - Writing test functions
   - Using assertions
   - Parametrized testing
   - Test organization

2. **Algorithm Analysis**:
   - Time and space complexity
   - When to use each algorithm
   - Trade-offs between algorithms

3. **Software Engineering Practices**:
   - Code organization
   - Testing strategies
   - Documentation
   - Containerization
   - CI/CD pipelines

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Add your algorithm implementation
4. Write comprehensive tests
5. Update documentation
6. Submit a pull request

## 📝 Notes

- **Exponential and Fibonacci Search**: Currently commented out in parametrized tests due to implementation details
- **Array Requirements**: Most algorithms require sorted arrays except Linear Search and Sentinel Linear Search
- **Best First Search**: Requires graph representation and heuristic function

## 🧮 Algorithm Complexity Visualization

```
Performance Comparison (n = 1,000,000 elements):

Linear Search:     ████████████████████ 1,000,000 operations
Jump Search:       ████ 1,000 operations  
Binary Search:     ██ 20 operations
Interpolation:     █ 6 operations (best case)
```

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure `Search_Algo` is a proper Python package with `__init__.py`
2. **Test Discovery**: PyTest looks for files starting with `test_` or ending with `_test.py`
3. **Module Path**: Run tests from project root directory

### Debug Tips

```bash
# Run with debugging output
pytest -s -v

# Stop on first failure
pytest -x

# Run last failed tests only
pytest --lf

# Show local variables in tracebacks
pytest -l
```

---

Made with ❤️ for learning Data Structures, Algorithms, and Testing Best Practices