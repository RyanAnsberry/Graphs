from graph import Graph
from queue import Queue

# breath first treversal
# returns array of all paths related to given node
def bft_find_all_paths(graph, starting_node):
    # set up queue, visited, and a list of paths
	queue = Queue()
	queue.enqueue([starting_node])
	visited = set()
	all_paths = []

	while queue.size() > 0:
		path = queue.dequeue()
		node = path[-1]

		if node not in visited:
			visited.add(node)
			if len(graph.nodes[node]) > 0:
				all_paths = []
			for new_node in graph.nodes[node]:
				new_path = list(path)
				new_path.append(new_node)
				if len(graph.nodes[new_node]) == 0:
					all_paths.append(new_path)
				else:
					queue.enqueue(new_path)

	return all_paths

def earliest_ancestor(ancestors, starting_node):
	graph = Graph()

	# populates graph
	for ancestor in ancestors:
		graph.add_edge(ancestor[0], ancestor[1])


	all_paths = bft_find_all_paths(graph, starting_node)

	# assigns -1 if no paths exist otherwise assigns last value of first path 
	answer = -1 if len(all_paths) == 0 else all_paths[0][-1]

	if len(all_paths) > 1:
		for i in range(len(all_paths)-1):
			if all_paths[i+1][-1] < answer:
				answer = all_paths[i+1][-1]

	return answer


# (parent, child)

