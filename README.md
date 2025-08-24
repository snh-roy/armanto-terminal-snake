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

## Installation

Follow these steps to set up the Snake game as a terminal command.

1. Fork and Clone the Repository
Fork this repository on GitHub by clicking the "Fork" button.
Clone the repository to your local machine:
git clone https://github.com/sneharoy/armanto-terminal-snake.git
cd armanto-terminal-snake


2. Make the Script Executable
Add execute permissions to snake.py:
chmod +x snake.py



3. Move to a PATH Directory
Move the script to a directory in your system's PATH (e.g., /usr/local/bin):
sudo mv snake.py /usr/local/bin/snake

Enter your administrator password when prompted.


4. (Optional) Create an Alias
For a shorter command, add an alias to your shell configuration file (e.g., ~/.bashrc for Bash or ~/.zshrc for Zsh):
echo "alias snake='snake'" >> ~/.bashrc
source ~/.bashrc



For Zsh users, replace ~/.bashrc with ~/.zshrc.

## Windows Users

- Ensure windows-curses is installed (see Prerequisites).
- Create a batch file to run the game:
echo @echo off > snake.bat
echo python %USERPROFILE%\path\to\snake.py >> snake.bat

- Move snake.bat to a directory in your PATH (e.g., C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\Scripts).
- Run snake in Command Prompt.

## Alternative for No sudo Access

If you don’t have sudo privileges, use a user-writable directory:
Create a bin directory in your home folder:
mkdir ~/bin

Move the script:
mv snake.py ~/bin/snake

Add ~/bin to your PATH:
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

(For Zsh, use ~/.zshrc instead of ~/.bashrc.)

## Usage 

Run the game by typing on terminal:
snake 
 

Controls:
Arrow keys or WASD to move the snake
- q to quit
- r to restart after game over


The snake moves automatically; guide it to eat food (☃) to increase your score.

## Troubleshooting

- "Terminal too small" error: Resize your terminal to at least 40x10 characters.

- No colors: Ensure your terminal supports colors (e.g., use xterm or gnome-terminal).

- Permission denied with sudo: Use the alternative ~/bin setup.
- Windows issues: Verify windows-curses is installed and Python is in your PATH.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Suggestions for new features or bug fixes are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
