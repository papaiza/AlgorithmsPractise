graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
def dfs_loop(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		print("Vertex: " + str(vertex))
		if vertex not in visited:
			visited.add(vertex)
			print("Visited: " + str(visited))
			stack.extend(graph[vertex] - visited)
			print("Stack: " + str(stack))
	return visited


def dfs_recursive(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	for next in graph[start] - visited:
		dfs_recursive(graph, next, visited)
	return visited

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))


# dfs_loop(graph, 'A')
# print(dfs_recursive(graph, 'C'))
print("All possible paths from A to F: " + str(list(dfs_paths(graph, 'A','F'))))

