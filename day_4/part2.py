def count_xmas(grid):
    # Define dimensions
    rows = len(grid)
    cols = len(grid[0])

    # Word to search
    word = "XMAS"
    word_len = len(word)

    # All 8 possible directions (row_step, col_step)
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (-1, -1),  # up-left
        (1, -1),  # down-left
        (-1, 1),  # up-right
    ]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_direction(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if not is_valid(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    # Count occurrences
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count


# Example usage with your sample grid:
with open("input.txt") as f:
    input_str = f.read()

# Convert the grid to a list of lists
grid = [row for row in input_str.split("\n")]

# Count the occurrences of "XMAS"
print("Total XMAS occurrences:", count_xmas(grid))
