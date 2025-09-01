import pytest
from Search_Algo.best_first_search import best_first_search

def test_best_first_search_found():
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0, 'E': 0}
    
    assert best_first_search(graph, 'A', 'D', heuristic) is True
    assert best_first_search(graph, 'A', 'E', heuristic) is True

def test_best_first_search_not_found():
    graph = {
        'A': ['B'],
        'B': [],
    }
    heuristic = {'A': 1, 'B': 0}
    
    assert best_first_search(graph, 'A', 'Z', heuristic) is False
