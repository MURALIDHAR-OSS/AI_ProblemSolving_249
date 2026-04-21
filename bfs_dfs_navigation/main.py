from collections import deque

# Graph (example)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

# DFS
def dfs(graph, start, goal, path=[], visited=set()):
    path = path + [start]

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result

    return None


# Input
start = input("Enter start node: ")
goal = input("Enter goal node: ")

print("\nBFS Path:", bfs(graph, start, goal))
print("DFS Path:", dfs(graph, start, goal))
