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
		# init first path vertex
		path = queue.dequeue()
		node = path[-1]
		neighbors = graph.get_neighbors(node)
		print(f"Curr Node: {node}")

		# check if node has been visited
		if node not in visited:
			# add to visited
			visited.add(node)
			print(f"Neighbors: {neighbors}")
			# check for neighbor verteces/nodes
			if len(neighbors) > 0:
				all_paths = []
				print(f"clear all_paths {all_paths}")
			# append new nodes to new path
			for new_node in neighbors:
				new_path = list(path)
				new_path.append(new_node)
				print(f"New path: {new_path}")
				# if new node has no neighbors
				if len(graph.nodes[new_node]) == 0:
					all_paths.append(new_path)
					print(f"all_paths with new path {all_paths}")
				else:
					queue.enqueue(new_path)
					print(f"enque new path {queue.queue}")

	return all_paths

def earliest_ancestor(ancestors, starting_node):
	graph = Graph()

	# populates graph
	for ancestor in ancestors:
		graph.add_edge(ancestor[0], ancestor[1])

	all_paths = bft_find_all_paths(graph, starting_node)
	print(f"All paths: {all_paths}")

	# assigns -1 if no paths exist otherwise assigns last value of first path 
	answer = -1 if len(all_paths) == 0 else all_paths[0][-1]

	if len(all_paths) > 1:
		for i in range(len(all_paths)-1):
			if all_paths[i+1][-1] < answer:
				answer = all_paths[i+1][-1]

	return answer


# (parent, child)
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))