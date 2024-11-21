from enum import Enum
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def path_to_directions(path):
    """
    Converts a list of cells representing a path into a list of directions.

    :param path: List of tuples (row, col) representing the path
    :return: List of Direction enums representing the directions
    """
    directions = []
    for i in range(len(path) - 1):
        current = path[i]
        next_cell = path[i + 1]

        # Calculate the direction based on the difference in coordinates
        row_diff = next_cell[0] - current[0]
        col_diff = next_cell[1] - current[1]

        if row_diff == -1 and col_diff == 0:
            directions.append(Direction.UP)
        elif row_diff == 1 and col_diff == 0:
            directions.append(Direction.DOWN)
        elif row_diff == 0 and col_diff == -1:
            directions.append(Direction.LEFT)
        elif row_diff == 0 and col_diff == 1:
            directions.append(Direction.RIGHT)
        elif current[0] == 14 and current[1] == 0:
            directions.append(Direction.LEFT)
        elif current[0] == 14 and current[1] == 27:
            directions.append(Direction.RIGHT)

    return directions