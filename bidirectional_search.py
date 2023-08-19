from collections import defaultdict, deque

def build_graph(word_list):
    graph = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            wildcard = word[:i] + '*' + word[i+1:]
            graph[wildcard].append(word)
    return graph

def bidirectional_search(graph, beginWord, endWord):
    if endWord not in graph:
        return []

    forward_queue = deque([(beginWord, 1)])
    backward_queue = deque([(endWord, 1)])

    forward_visited = {beginWord: 1}
    backward_visited = {endWord: 1}

    while forward_queue and backward_queue:
        intermediate_word = bfs(graph, forward_queue, forward_visited, backward_visited)
        if intermediate_word:
            path = get_path(forward_visited, backward_visited, intermediate_word)
            return path

        intermediate_word = bfs(graph, backward_queue, backward_visited, forward_visited)
        if intermediate_word:
            path = get_path(forward_visited, backward_visited, intermediate_word)
            return path

    return []

def bfs(graph, queue, visited, opposite_visited):
    word, level = queue.popleft()

    for i in range(len(word)):
        wildcard = word[:i] + '*' + word[i+1:]
        neighbors = graph[wildcard]

        for neighbor in neighbors:
            if neighbor in opposite_visited:
                return neighbor

            if neighbor not in visited:
                visited[neighbor] = level + 1
                queue.append((neighbor, level + 1))

    return None

def get_path(forward_visited, backward_visited, intermediate_word):
    path = []
    while intermediate_word:
        path.append(intermediate_word)
        intermediate_word = bfs_shortest_neighbor(forward_visited, backward_visited, intermediate_word)
    return path[::-1]

def bfs_shortest_neighbor(forward_visited, backward_visited, word):
    for i in range(len(word)):
        wildcard = word[:i] + '*' + word[i+1:]
        neighbors = forward_visited.get(wildcard, [])
        for neighbor in neighbors:
            if backward_visited.get(neighbor):
                return neighbor
    return None

# Example usage
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hit"
endWord = "cog"

graph = build_graph(word_list)
path = bidirectional_search(graph, beginWord, endWord)
print("Shortest path:", path)
