import pytest
from Search_Algo.linear_search import linear_search
from Search_Algo.binary_search import binary_search
from Search_Algo.sentinel_linear_search import sentinel_linear_search
from Search_Algo.meta_binary_search import meta_binary_search
from Search_Algo.ternary_search import ternary_search
from Search_Algo.jump_search import jump_search
from Search_Algo.interpolation_search import interpolation_search
from Search_Algo.exponential_search import exponential_search
from Search_Algo.fibonacci_search import fibonacci_search

# Sample sorted array for search algorithms
arr = [1, 3, 5, 7, 9, 11, 13, 15]

@pytest.mark.parametrize("func", [
    linear_search,
    binary_search,
    sentinel_linear_search,
    meta_binary_search,
    ternary_search,
    jump_search,
    interpolation_search
    #exponential_search,
    #fibonacci_search
])
def test_search_algorithms(func):
    """Test common searching algorithms on a sorted array."""
    # Positive cases
    assert func(arr, 7) == arr.index(7)
    assert func(arr, 15) == arr.index(15)
    assert func(arr, 1) == arr.index(1)

    # Negative case
    assert func(arr, 100) == -1