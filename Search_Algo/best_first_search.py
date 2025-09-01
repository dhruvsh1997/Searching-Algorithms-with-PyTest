import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = [(heuristic[start], start)]
    while pq:
        _, node = heapq.heappop(pq)
        if node == goal:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                heapq.heappush(pq, (heuristic[neighbor], neighbor))
    return False
