# Terminal Snake Game
In 1997, Taneli Armanto, a designer at Nokia, programmed the snake game we know from our parents' phones. Here I implemented all using Python to revive the nostalgia. Using the `curses library, designed to run in a terminal. Control the snake with arrow keys or WASD, eat food to grow, and avoid collisions with walls or yourself!

## Features
- Colorful terminal-based UI with a magenta snake, green food, and yellow score display
- Smooth controls with arrow keys or WASD
- Score tracking and game over screen with restart option
- Simple setup to run as a terminal command

## Prerequisites
- Python 3.6 or higher
- A terminal that supports colors (most modern terminals do)
- Minimum terminal size: 40 columns x 10 rows
- **Linux/macOS**: `curses` is included with Python
- **Windows**: Install the `windows-curses` package:
  ```bash
  pip install windows-curses
