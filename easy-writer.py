# Easy Writer - A simple text editor for people who prefer minimalism over features.
# Importing the libraries
import curses
import os

# Initializing the curses window
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Creating a text buffer
buffer = []

# Creating a function to display the buffer on the screen
def display():
    screen.clear()
    for i, line in enumerate(buffer):
        screen.addstr(i, 0, line)
    screen.refresh()

# Creating a function to handle keyboard input
def input():
    global buffer
    # Getting the current cursor position
    y, x = screen.getyx()
    # Getting the key pressed
    key = screen.getch()
    # Handling different keys
    if key == curses.KEY_BACKSPACE: # Delete the previous character
        if x > 0: # If not at the beginning of the line
            buffer[y] = buffer[y][:x-1] + buffer[y][x:]
            screen.move(y, x-1)
        elif y > 0: # If at the beginning of the line and not the first line
            prev_line = buffer.pop(y)
            screen.move(y-1, len(buffer[y-1]))
            buffer[y-1] += prev_line
    elif key == curses.KEY_ENTER or key in [10, 13]: # Insert a new line
        buffer.insert(y+1, buffer[y][x:])
        buffer[y] = buffer[y][:x]
        screen.move(y+1, 0)
    elif key == curses.KEY_UP: # Move the cursor up
        if y > 0:
            screen.move(y-1, x)
    elif key == curses.KEY_DOWN: # Move the cursor down
        if y < len(buffer) - 1:
            screen.move(y+1, x)
    elif key == curses.KEY_LEFT: # Move the cursor left
        if x > 0:
            screen.move(y, x-1)
    elif key == curses.KEY_RIGHT: # Move the cursor right
        if x < len(buffer[y]):
            screen.move(y, x+1)
    elif key == curses.KEY_F1: # Save the buffer to a file
        # Asking the user for a file name
        screen.clear()
        screen.addstr(0, 0, "Enter file name: ")
        screen.refresh()
        # Reading the file name
        curses.echo()
        file_name = screen.getstr(1, 0).decode()
        curses.noecho()
        # Writing the buffer to the file
        with open(file_name, "w") as f:
            for line in buffer:
                f.write(line + "\n")
        # Showing a confirmation message
        screen.clear()
        screen.addstr(0, 0, f"File {file_name} saved successfully.")
        screen.refresh()
        screen.getch()
    elif key == curses.KEY_F2: # Exit the program
        # Restoring the terminal settings
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()
        # Exiting the program
        exit()
    elif 0 <= key <= 255: # Insert a printable character
        buffer[y] = buffer[y][:x] + chr(key) + buffer[y][x:]
        screen.move(y, x+1)
    # Displaying the buffer
    display()

# Adding an empty line to the buffer
buffer.append("")

# Displaying the buffer
display()

# Entering the main loop
while True:
    input()
