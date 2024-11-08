import random

# Set up constants for the grid
GRID_SIZE = 5
HIT = "X"
MISS = "O"
EMPTY = "."

# Initialize the grid
def create_grid(size):
    return [[EMPTY for _ in range(size)] for _ in range(size)]

# Print the grid to visualize the game
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Place a ship randomly on the grid
def place_ship(grid):
    ship_row = random.randint(0, GRID_SIZE - 1)
    ship_col = random.randint(0, GRID_SIZE - 1)
    return ship_row, ship_col

# Main game loop
def play_battleship():
    grid = create_grid(GRID_SIZE)
    ship_row, ship_col = place_ship(grid)
    attempts = 0

    print("Welcome to Battleship!")
    print("Try to sink the ship by guessing its location.")
    print_grid(grid)

    while True:
        try:
            guess_row = int(input("Enter row (0 to 4): "))
            guess_col = int(input("Enter column (0 to 4): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess_row < 0 or guess_row >= GRID_SIZE or guess_col < 0 or guess_col >= GRID_SIZE:
            print("Guess out of bounds! Try again.")
            continue

        attempts += 1

        if guess_row == ship_row and guess_col == ship_col:
            print("Hit! You sunk the battleship!")
            grid[guess_row][guess_col] = HIT
            print_grid(grid)
            print(f"You won in {attempts} attempts!")
            break
        elif grid[guess_row][guess_col] == MISS:
            print("You already guessed that location. Try again.")
        else:
            print("Miss!")
            grid[guess_row][guess_col] = MISS
            print_grid(grid)

# Run the game
play_battleship()
