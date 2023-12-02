"""
grid_generation.py - Authored by Arsalan Kazmi

Generates the grid for the Connect 4 game.
It's not exactly one function because if it was all one monolithic function it would be kind of inefficient? Idk just work with it
"""


def get_valid_row_or_col_input(min_val: int, max_val: int, rows_or_cols: str) -> int:
    """
    Prints a prompt asking for the number of rows or columns required, and verifies
    the input to ensure it falls within the specified range.

    Parameters:
    - min_val (int): The minimum allowed number of rows or columns.
    - max_val (int): The maximum allowed number of rows or columns.
    - rows_or_cols (str): The prompt string, e.g., "how many rows" or "how many columns".

    Returns:
    - user_input (int): The validated input provided by the user.
    """
    input_message = f"How many {rows_or_cols}? (minimum {min_val}, maximum {max_val})"

    while True:
        try:
            user_input = int(input(f"{input_message}\n> "))
            if min_val <= user_input <= max_val:
                break
            else:
                print(f"Sorry, the number must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting.")

    return user_input


def ask_for_grid_size() -> tuple[int, int]:
    """
    Calls `get_valid_row_or_col_input` for both rows and columns.

    Parameters:
    - None

    Returns:
    - Tuple[int, int]
        - rows (int): The validated amount of rows.
        - cols (int): The validated amount of columns.
    """
    MIN_ROWS = 8
    MAX_ROWS = 18
    MIN_COLS = 6
    MAX_COLS = 14

    rows = get_valid_row_or_col_input(MIN_ROWS, MAX_ROWS, "rows")
    cols = get_valid_row_or_col_input(MIN_COLS, MAX_COLS, "columns")

    return rows, cols


def generate_grid(rows: int, cols: int) -> list[list[str]]:
    """
    Generates a 2D grid represented as a list of lists.

    Parameters:
    - rows (int): The number of rows in the grid.
    - cols (int): The number of columns in the grid.

    Returns:
    - grid (List[List[str]]): The generated grid.
    """
    grid = [['[ ]' for _ in range(cols)] for _ in range(rows)]
    return grid


def print_grid(grid: list[list[str]]):
    """
    Prints the generated grid line by line.

    Parameters:
    - grid (List[List[str]]): The generated grid, to be printed.

    Returns:
    - None
    """
    for row in grid:
        print(" ".join(row))
    print()


def main():
    """
    I hope you know what a main function is.

    Parameters:
    - None

    Returns:
    - None
    """
    grid_size = ask_for_grid_size()
    print(f"Selected grid size: {grid_size}")

    grid = generate_grid(rows=grid_size[0], cols=grid_size[1])
    print_grid(grid)

    # Now we can proceed with the Connect 4 game logic, updating the grid elements with 'O' and 'X' for red and yellow

if __name__ == "__main__":
    main()

"""
Grid generation output looks like this:

```
How many rows? (minimum 8, maximum 18)
> How many columns? (minimum 6, maximum 14)
> Selected grid size: (10, 10)
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
[ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ]
```
"""
