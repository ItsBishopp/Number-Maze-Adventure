import random
import time
import turtle

# Set up the grid and maze size
Size = 15
Cell_Size = 25

# Function to generate the maze with random numbers, obstacles, and power-ups
def generate_maze():
    # Define the special symbols used in the maze
    symbols = ['R', 'G', 'G', 'white']  # Use 'R' for red obstacles, 'G' for green obstacles
    maze = [[random.choice(symbols + [random.randint(1, 9)]) for _ in range(Size)] for _ in range(Size)]
    return maze

# Function to draw a rectangle with a given color at a specific position
def draw_rectangle(x, y, color):
    # Draw a rectangle of the specified color at the given (x, y) position
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(Cell_Size)
        turtle.left(90)
    turtle.end_fill()

# Function to draw the maze on the screen
def draw_maze(maze, player_row, player_col):
    # Clear the previous drawings and draw the entire maze with updated player's position
    turtle.clear()
    turtle.speed(0)  # Fastest drawing speed
    for row in range(Size):
        for col in range(Size):
            x, y = col * Cell_Size - (Cell_Size * Size) // 2, (Size - row - 1) * Cell_Size - (Cell_Size * Size) // 2
            if row == player_row and col == player_col:
                # Draw the player's icon (turtle) at their position
                turtle.shape('turtle')
                turtle.color('blue')
                turtle.penup()
                turtle.goto(x + Cell_Size // 2, y + Cell_Size // 2)
                turtle.stamp()
            elif maze[row][col] == 'R':
                draw_rectangle(x, y, 'red')  # Color for red obstacles
            elif maze[row][col] == 'G':
                draw_rectangle(x, y, 'green')  # Color for green obstacles
            else:
                draw_rectangle(x, y, 'white')  # Color for the correct path
    turtle.update()

# Main game loop
def main():
    turtle.setup(Cell_Size * Size, Cell_Size * Size)
    turtle.title("Number Maze Adventure")
    turtle.bgcolor('white')
    turtle.tracer(0)  # Turn off animation for faster drawing

    # Generate the maze and display it
    maze = generate_maze()
    player_row, player_col = 0, 0  # Initialize the player's position at the top-left corner
    draw_maze(maze, player_row, player_col)
    turtle.update()

    # Define the player's starting position, score, and timer
    score = 0
    # Record the start time
    start_time = time.time()  

    # Welcome the player to the Number Maze Adventure!
    welcome_message = "Embark on the thrilling 'Number Maze Adventure' – conquer obstacles, gather numbers, and master the labyrinth's enigmas. Can you reach the end and claim victory? Welcome, adventurer!"
    print(welcome_message)

    print("\n-------------")
    print("Get ready...")
    delay = random.uniform(0.5, 1.0)
    time.sleep(delay)
    print()
  
    # Main game loop
    while True:
        # Process the player's move and update their position
        move = input("Enter your move (w-up, s-down, a-left, d-right, q-quit): ")
        if move == 'w':
            player_row -= 1
        elif move == 's':
            player_row += 1
        elif move == 'a':
            player_col -= 1
        elif move == 'd':
            player_col += 1
        elif move == 'q':
            print("Quitting the game. Goodbye!")
            break
        else:
            print("Invalid move. Please try again.")
            continue

        # Check if the player has reached the end of the maze
        if player_row == Size - 1 and player_col == Size - 1:
            elapsed_time = time.time() - start_time
            print("Congratulations! You reached the end of the maze.")
            print("Your final score is:", score)
            print("Time taken:", round(elapsed_time, 2), "seconds.")
            break

        # Check if the player's position is within the maze boundaries
        if not (0 <= player_row < Size and 0 <= player_col < Size):
            print("Out of bounds. Please try again.")
            continue

        # Check for obstacles in the maze (red and green cells)
        if maze[player_row][player_col] in ['R', 'G']:
            print("You hit an obstacle! Try a different path.")
            continue

        # Update the score based on the number or power-up in the current cell
        cell_content = maze[player_row][player_col]
        if isinstance(cell_content, int):
            score += cell_content

        maze[player_row][player_col] = 'X'
        draw_maze(maze, player_row, player_col)
        turtle.update()

        print("Your current score is:", score)

if __name__ == "__main__":
    main()
