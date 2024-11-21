import heapq
from collections import deque
class Graph:
    def __init__(self, gameBoard, algorithm = None):
        self.graph = self.build_graph(gameBoard)
        self.algorithm = algorithm

    def build_graph(self, board):
        """
            Constructs a graph representation of the Pacman game board.

            :param board: 2D list of Cell objects representing the game board
            :return: A dictionary representing the graph
            """
        rows = len(board)
        cols = len(board[0])
        graph = {}

        def is_valid_neighbor(r, c):
            """Checks if the cell at (r, c) is valid and 'empty'."""
            return 0 <= r < rows and 0 <= c < cols and board[r][c].type == "Empty"

        # Define directions for neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c].type == "Empty":
                    # Add this cell to the graph
                    neighbors = []
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if is_valid_neighbor(nr, nc):
                            neighbors.append((nr, nc))
                    if (r,c) == (14,0):
                        neighbors.append((14,27))
                    elif (r,c) == (14,27):
                        neighbors.append((14,0))
                    graph[(r, c)] = neighbors
        return graph

    def shortest_path(self, start, goal, ghost=None, pellets=[]):
        if self.algorithm == "dfs":
            return self.dfs_shortest_path(start, goal, ghost, pellets)
        elif self.algorithm == "bfs":
            return self.bfs_shortest_path(start, goal, ghost, pellets)
        elif self.algorithm == "ucs":
            return self.ucs_shortest_path(start, goal, ghost, pellets)
        else:
            return self.a_star_shortest_path(start, goal, ghost, pellets)

    def ucs_shortest_path(self, start, goal, ghost=None, pellets=[]):
        """
        Finds the shortest path from start to goal using Uniform Cost Search.

        :param start: Tuple (row, col) representing the start cell
        :param goal: Tuple (row, col) representing the goal cell
        :param ghost: Tuple (row, col) representing the ghost cell
        :param cell_costs: Dictionary mapping each cell to its movement cost
        :return: List of cells representing the shortest path, or None if unreachable
        """
        # Priority queue: (cumulative_cost, current_cell, path_so_far)
        priority_queue = []
        heapq.heappush(priority_queue, (0, start, [start]))

        # Visited set to avoid revisiting nodes
        visited = set()

        while priority_queue:
            # Pop the cell with the lowest cumulative cost
            current_cost, current_cell, path = heapq.heappop(priority_queue)

            # If the cell has already been visited, skip it
            if current_cell in visited:
                continue
            visited.add(current_cell)

            # Check if the goal is reached
            if current_cell == goal:
                return path  # Return the path to the goal

            # Expand neighbors
            for neighbor in self.graph.get(current_cell, []):
                if neighbor not in visited:
                    # Calculate the cost to move to this neighbor
                    if ghost is not None:
                        neighbor_cost = 1 if neighbor in pellets else 0
                        neighbor_distance = 1 / self.getDistanceFromStartToTarget(neighbor, ghost)
                        new_cost = current_cost + neighbor_cost
                    else:
                        new_cost = current_cost + 1
                    # Add the neighbor to the priority queue with the updated cost and path
                    heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

        # If the goal is not reachable, return None
        return None

    def dfs_shortest_path(self, start, goal, ghost=None, pellets=[]):
        """
        Finds a path from start to goal using Depth-First Search (DFS).
        Penalizes paths that are closer to the ghost if provided.

        :param start: Tuple (row, col) representing the start cell
        :param goal: Tuple (row, col) representing the goal cell
        :param ghost: Tuple (row, col) representing the ghost cell
        :param cell_costs: Dictionary mapping each cell to its movement cost
        :return: List of cells representing the path, or None if unreachable
        """
        # Stack: (current_cell, path_so_far, cumulative_cost)
        stack = [(start, [start], 0)]
        visited = set()
        best_path = None
        best_cost = float('inf')

        while stack:
            current_cell, path, current_cost = stack.pop()

            # Skip visited nodes
            if current_cell in visited:
                continue
            visited.add(current_cell)

            # Check if the goal is reached
            if current_cell == goal:
                if current_cost < best_cost:
                    best_path = path
                    best_cost = current_cost
                continue

            # Expand neighbors
            for neighbor in self.graph.get(current_cell, []):
                if neighbor not in visited:
                    # Compute cost for this neighbor
                    base_cost = 1 if neighbor in pellets else 0  # Default cost is 1
                    ghost_penalty = (
                        (1 / self.getDistanceFromStartToTarget(neighbor, ghost)) * 50 if ghost else 0
                    )
                    new_cost = current_cost + base_cost + ghost_penalty

                    # Add to stack
                    stack.append((neighbor, path + [neighbor], new_cost))

        return best_path

    def bfs_shortest_path(self, start, goal, ghost=None,pellets=[]):
        """
        Finds the shortest path from start to goal using Breadth-First Search (BFS).
        Penalizes paths that are closer to the ghost if provided.

        :param start: Tuple (row, col) representing the start cell
        :param goal: Tuple (row, col) representing the goal cell
        :param ghost: Tuple (row, col) representing the ghost cell
        :param cell_costs: Dictionary mapping each cell to its movement cost (ignored in BFS).
        :return: List of cells representing the shortest path, or None if unreachable.
        """
        # Queue: (current_cell, path_so_far)
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current_cell, path = queue.popleft()

            # Skip if already visited
            if current_cell in visited:
                continue
            visited.add(current_cell)

            # Check if the goal is reached
            if current_cell == goal:
                return path

            # Expand neighbors
            for neighbor in self.graph.get(current_cell, []):
                if neighbor not in visited:
                    # Add the neighbor to the queue with the updated path
                    queue.append((neighbor, path + [neighbor]))

        # Return None if the goal is not reachable
        return None

    def a_star_shortest_path(self, start, goal, ghost=None, pellets=[]):
        """
        Finds the shortest path from start to goal using A* Search.
        Penalizes paths that are closer to the ghost if provided.

        :param start: Tuple (row, col) representing the start cell.
        :param goal: Tuple (row, col) representing the goal cell.
        :param ghost: Tuple (row, col) representing the ghost cell (optional).
        :param cell_costs: Dictionary mapping each cell to its movement cost (optional).
        :return: List of cells representing the shortest path, or None if unreachable.
        """
        # Priority queue: (f_score, current_cell, path_so_far, g_score)
        open_set = []
        heapq.heappush(open_set, (0, start, [start], 0))

        visited = set()

        while open_set:
            # Pop the node with the lowest f_score
            _, current_cell, path, g_score = heapq.heappop(open_set)

            # If already visited, skip it
            if current_cell in visited:
                continue
            visited.add(current_cell)

            # Check if the goal is reached
            if current_cell == goal:
                return path

            # Expand neighbors
            for neighbor in self.graph.get(current_cell, []):
                if neighbor not in visited:
                    # Calculate g (current path cost) and h (heuristic cost)
                    g = g_score + 1 if neighbor in pellets else 0  # Movement cost to neighbor
                    h = self.manhattan_distance(neighbor, goal)  # Heuristic (Manhattan distance)

                    # Add ghost penalty if ghost is provided
                    if ghost:
                        ghost_penalty = 50 * (1 / max(self.manhattan_distance(neighbor, ghost), 1))
                        h += ghost_penalty

                    f = g + h  # Total cost (f = g + h)

                    # Add to the priority queue
                    heapq.heappush(open_set, (f, neighbor, path + [neighbor], g))

        # Return None if the goal is not reachable
        return None

    def getDistanceFromStartToTarget(self, start, target):
        if self.algorithm == "dfs":
            return self.getDistanceFromStartToTargetDFS(start, target)
        elif self.algorithm == "bfs":
            return self.getDistanceFromStartToTargetBFS(start, target)
        elif self.algorithm == "ucs":
            return self.getDistanceFromStartToTargetUCS(start, target)
        else:
            return self.getDistanceFromStartToTargetDFS(start, target)

    def getDistanceFromStartToTargetUCS(self, start, target):
        """
        Finds the shortest path from start to goal using Uniform Cost Search,
        assuming all edges have the same cost.

        :param start: Starting node
        :param target: Goal node
        :return: List of nodes representing the shortest path, or None if unreachable
        """
        # Queue for BFS: stores (current_node, path_so_far)
        queue = deque([(start, [start])])

        # Visited set to prevent revisiting nodes
        visited = set()

        while queue:
            # Dequeue the front of the queue
            current_node, path = queue.popleft()

            # Skip if already visited
            if current_node in visited:
                continue
            visited.add(current_node)

            # Check if we reached the goal
            if current_node == target:
                return len(path)

            # Enqueue all unvisited neighbors
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        # Return None if the goal is not reachable
        return 0

    def getDistanceFromStartToTargetDFS(self, start, target):
        """
        Finds the shortest path from start to target using Depth-First Search.
        Returns the length of the path.

        :param start: Starting node
        :param target: Goal node
        :return: Length of the shortest path, or 0 if unreachable
        """
        stack = [(start, [start])]
        visited = set()

        while stack:
            current_node, path = stack.pop()

            if current_node in visited:
                continue
            visited.add(current_node)

            # Check if the target is reached
            if current_node == target:
                return len(path)

            # Push neighbors onto the stack
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        # Return 0 if the target is not reachable
        return 0

    def getDistanceFromStartToTargetBFS(self, start, target):
        """
        Finds the shortest path from start to target using Breadth-First Search (BFS).
        Returns the length of the path.

        :param start: Starting node.
        :param target: Goal node.
        :return: Length of the shortest path, or 0 if unreachable.
        """
        queue = deque([(start, 0)])  # Queue stores (current_node, current_distance)
        visited = set()

        while queue:
            current_node, distance = queue.popleft()

            if current_node in visited:
                continue
            visited.add(current_node)

            # Check if the target is reached
            if current_node == target:
                return distance + 1

            # Push neighbors onto the queue
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

        # Return 0 if the target is not reachable
        return 0

    def getDistanceFromStartToTargetAStar(self, start, target, ghost=None, cell_costs={}):
        """
        Finds the shortest path distance from start to target using A* Search.
        :param start: Starting cell (row, col).
        :param target: Goal cell (row, col).
        :param ghost: Tuple (row, col) representing the ghost cell (optional).
        :param cell_costs: Dictionary mapping each cell to its movement cost (optional).
        :return: Distance of the shortest path, or -1 if unreachable.
        """
        open_set = []
        heapq.heappush(open_set, (0, start, 0))  # (f_score, current_cell, g_score)

        visited = set()

        while open_set:
            _, current_cell, g_score = heapq.heappop(open_set)

            if current_cell in visited:
                continue
            visited.add(current_cell)

            # Check if the target is reached
            if current_cell == target:
                return g_score

            # Expand neighbors
            for neighbor in self.graph.get(current_cell, []):
                if neighbor not in visited:
                    g = g_score + cell_costs.get(neighbor, 1)  # Movement cost to neighbor
                    h = self.manhattan_distance(neighbor, target)  # Heuristic
                    if ghost:
                        ghost_penalty = 50 * (1 / max(self.manhattan_distance(neighbor, ghost), 1))
                        h += ghost_penalty
                    f = g + h
                    heapq.heappush(open_set, (f, neighbor, g))

        return -1  # Return -1 if the target is not reachable

    def manhattan_distance(self, cell, target):
        """
        Calculates the Manhattan distance between two cells.
        :param cell: Tuple (row, col) of the current cell.
        :param target: Tuple (row, col) of the target cell.
        :return: Manhattan distance.
        """
        return abs(cell[0] - target[0]) + abs(cell[1] - target[1])
