from Sprites.Direction import Direction
from collections import deque

class TreeNode:
    def __init__(self, row, col, direction: Direction=None):
        self.row = row
        self.col = col
        self.direction = direction  # Direction from the parent node
        self.children = []

def get_directions_to_cell(root, target):
    return get_directions_to_cell_bfs(root, target)
def generate_tree(board, coords) -> TreeNode:
    return generate_tree_bfs(board, coords)


def get_directions_to_cell_bfs(root, target):
    queue = deque([(root, [])])  # Queue stores tuples of (current_node, path_to_node)

    while queue:
        current_node, path = queue.popleft()  # Dequeue the front element

        # If the target cell is reached, return the path
        if current_node.row == target.row and current_node.col == target.col:
            return path

        # Traverse each child node
        for child in current_node.children:
            new_path = path + [(child.row, child.col, child.direction)]
            queue.append((child, new_path))  # Enqueue the child with the updated path

    # Return None if the target is not reachable
    return None

def get_directions_to_cell_dfs(root, target):
    path = []

    def dfs(node):
        # Base case: if we have reached the target cell
        if node.row == target.row and node.col == target.col:
            return True

        # Traverse each child node
        for child in node.children:
            # Add the direction to the path
            path.append((child.row, child.col, child.direction))

            # Recursively search in this child's subtree
            if dfs(child):
                return True  # If the target is found, bubble up the success

            # Backtrack if this path does not lead to the target
            path.pop()

        return False

    # Start DFS from the root node
    if dfs(root):
        return path  # Return the path if the target was found
    else:
        return None  # Return None if the target is not reachable


def generate_tree_dfs(board, coords) -> TreeNode:
    root = TreeNode(coords[1], coords[0])
    visited = set()

    def dfs(node):
        row, col = node.row, node.col
        visited.add((row, col))

        # Define movement directions (up, down, left, right) and their labels
        directions = [
            (-1, 0, Direction.LEFT),
            (1, 0, Direction.RIGHT),
            (0, -1, Direction.UP),
            (0, 1, Direction.DOWN)
        ]

        for dc, dr, direction in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and
                    (new_row, new_col) not in visited and board[new_row][new_col].type == "Empty"):

                # Create a new tree node for this cell with the direction set
                child_node = TreeNode(new_row, new_col, direction=direction)
                node.children.append(child_node)

                # Recursively expand this cell
                dfs(child_node)

    # Start DFS from the root node
    dfs(root)
    return root

def generate_tree_bfs(board, coords):
    root = TreeNode(coords[1], coords[0])
    visited = set()
    queue = deque([root])  # Queue for BFS

    while queue:
        current_node = queue.popleft()  # Dequeue the front element
        row, col = current_node.row, current_node.col
        visited.add((row, col))

        # Define movement directions (up, down, left, right) and their labels
        directions = [
            (-1, 0, Direction.LEFT),
            (1, 0, Direction.RIGHT),
            (0, -1, Direction.UP),
            (0, 1, Direction.DOWN)
        ]

        for dc, dr, direction in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and
                    (new_row, new_col) not in visited and board[new_row][new_col].type == "Empty"):

                # Create a new tree node for this cell with the direction set
                child_node = TreeNode(new_row, new_col, direction=direction)
                current_node.children.append(child_node)  # Add child to current node
                queue.append(child_node)  # Enqueue the child node

    return root