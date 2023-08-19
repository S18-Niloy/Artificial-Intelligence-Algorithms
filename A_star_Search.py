import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # cost from start to current node
        self.h = 0  # heuristic estimate of cost from current node to goal
        self.f = 0  # total estimated cost (f = g + h)

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    
    heapq.heappush(open_set, (start_node.f, start_node))
    
    while open_set:
        _, current_node = heapq.heappop(open_set)
        
        if (current_node.x, current_node.y) == (goal_node.x, goal_node.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()
            return path
        
        closed_set.add((current_node.x, current_node.y))
        
        neighbors = [
            (current_node.x - 1, current_node.y),
            (current_node.x + 1, current_node.y),
            (current_node.x, current_node.y - 1),
            (current_node.x, current_node.y + 1)
        ]
        
        for neighbor_x, neighbor_y in neighbors:
            if (
                0 <= neighbor_x < len(grid) and
                0 <= neighbor_y < len(grid[0]) and
                grid[neighbor_x][neighbor_y] == 0
            ):
                if (neighbor_x, neighbor_y) in closed_set:
                    continue
                
                neighbor = Node(neighbor_x, neighbor_y, parent=current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor, goal_node)
                neighbor.f = neighbor.g + neighbor.h
                
                if any(neighbor.f < item[1].f for item in open_set):
                    continue
                
                heapq.heappush(open_set, (neighbor.f, neighbor))
    
    return None  # No path found

# Example usage
if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    
    start = (0, 0)
    goal = (4, 4)
    
    path = astar(grid, start, goal)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found")
