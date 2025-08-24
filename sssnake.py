#!/usr/bin/env python3

import curses # This library handles keyboard input, screen output (moving cursors)
import random
import time

class SnakeGame:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.setup_screen()
        self.init_game()
        
    def setup_screen(self):
        # Initiliazing screen
        curses.curs_set(0)  # Hide cursor
        self.stdscr.nodelay(True)  # Non-blocking input
        self.stdscr.timeout(100)  # Refresh rate in ms (100ms = 0.1s delay)
        
        # Initialize colors
        curses.start_color()
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Snake, numbers like 1 is a pair number for snake, that's how it is called throughout
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)    # Food
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Score
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Border
        
        # screen dimensions
        self.height, self.width = self.stdscr.getmaxyx()
        
        # Game area (space for borders and score)
        self.game_height = self.height - 4
        self.game_width = self.width - 2
        
    def init_game(self):
        # snake starts in the middle, moving right
        start_y = self.game_height // 2
        start_x = self.game_width // 2
        
        self.snake = [
            [start_y, start_x],
            [start_y, start_x - 1],
            [start_y, start_x - 2]
        ]
        
        self.direction = [0, 1]  # Moving right [dy, dx]
        self.score = 0
        self.food = self.generate_food()
        self.game_over = False
        
    def generate_food(self):
        while True:
            food_y = random.randint(1, self.game_height - 2)
            food_x = random.randint(1, self.game_width - 2)
            if [food_y, food_x] not in self.snake:
                return [food_y, food_x]
    
    def draw_border(self):
        #Top and bottom borders
        for x in range(self.game_width):
            self.stdscr.addstr(0, x, '═', curses.color_pair(4))
            self.stdscr.addstr(self.game_height + 1, x, '═', curses.color_pair(4))
        
        #Left and right borders
        for y in range(self.game_height + 2):
            self.stdscr.addstr(y, 0, '║', curses.color_pair(4))
            self.stdscr.addstr(y, self.game_width - 1, '║', curses.color_pair(4))
        
        # Corners
        self.stdscr.addstr(0, 0, '╔', curses.color_pair(4))
        self.stdscr.addstr(0, self.game_width - 1, '╗', curses.color_pair(4))
        self.stdscr.addstr(self.game_height + 1, 0, '╚', curses.color_pair(4))
        self.stdscr.addstr(self.game_height + 1, self.game_width - 1, '╝', curses.color_pair(4))
    
    def draw_snake(self):
        #snake 
        for i, segment in enumerate(self.snake):
            y, x = segment
            if i == 0:  # Head
                char = '◉'
            else:  # Body
                char = '●'
            self.stdscr.addstr(y, x, char, curses.color_pair(1))
    
    def draw_food(self):
        #food 
        y, x = self.food
        self.stdscr.addstr(y, x, '☃', curses.color_pair(2))
    
    def draw_score(self):
        #score and instruction
        score_text = f"Score: {self.score}"
        instructions = "Use arrow keys to move, 'q' to quit"
        
        self.stdscr.addstr(self.game_height + 2, 2, score_text, curses.color_pair(3))
        
        #center the instruction
        instr_x = max(0, (self.width - len(instructions)) // 2)
        if self.game_height + 3 < self.height:
            self.stdscr.addstr(self.game_height + 3, instr_x, instructions)
    
    def handle_input(self):
        #keyboard input for exiting 
        key = self.stdscr.getch()
        
        if key == ord('q') or key == ord('Q'):
            self.game_over = True
            return
        
        # Arrow keys
        if key == curses.KEY_UP and self.direction != [1, 0]:
            self.direction = [-1, 0]
        elif key == curses.KEY_DOWN and self.direction != [-1, 0]:
            self.direction = [1, 0]
        elif key == curses.KEY_LEFT and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif key == curses.KEY_RIGHT and self.direction != [0, -1]:
            self.direction = [0, 1]
        
        # WASD keys as alternative
        elif key == ord('w') and self.direction != [1, 0]:
            self.direction = [-1, 0]
        elif key == ord('s') and self.direction != [-1, 0]:
            self.direction = [1, 0]
        elif key == ord('a') and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif key == ord('d') and self.direction != [0, -1]:
            self.direction = [0, 1]
    
    def move_snake(self):
        """Move the snake in the current direction"""
        head = self.snake[0].copy()
        head[0] += self.direction[0]
        head[1] += self.direction[1]
        
        # Check for wall collision
        if (head[0] <= 0 or head[0] >= self.game_height - 1 or
            head[1] <= 0 or head[1] >= self.game_width - 1):
            self.game_over = True
            return
        
        # Check for self collision
        if head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, head)
        
        # Check if food is eaten
        if head == self.food:
            self.score += 5
            self.food = self.generate_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
    
    def draw_game_over(self):
        game_over_text = "GAME OVER!"
        final_score = f"Final Score: {self.score}"
        restart_text = "Press 'r' to restart or 'q' to quit"
        
        # Calculate center positions
        center_y = self.height // 2
        center_x = self.width // 2
        
        # Draw game over messages
        self.stdscr.addstr(center_y - 1, center_x - len(game_over_text) // 2, 
                          game_over_text, curses.color_pair(2) | curses.A_BOLD)
        self.stdscr.addstr(center_y, center_x - len(final_score) // 2, 
                          final_score, curses.color_pair(3))
        self.stdscr.addstr(center_y + 1, center_x - len(restart_text) // 2, 
                          restart_text)
    
    def wait_for_restart(self):
        """Wait for user input after game over"""
        while True:
            key = self.stdscr.getch()
            if key == ord('r') or key == ord('R'):
                self.init_game()
                return True
            elif key == ord('q') or key == ord('Q'):
                return False
    
    def run(self):
        while True:
            self.stdscr.clear()
            
            if not self.game_over:
                # Handle input
                self.handle_input()
                
                # Move snake
                self.move_snake()
                
                # Draw everything
                self.draw_border()
                self.draw_snake()
                self.draw_food()
                self.draw_score()
                
            else:
                # Game over screen
                self.draw_border()
                self.draw_game_over()
                self.stdscr.refresh()
                
                # Wait for restart or quit
                if not self.wait_for_restart():
                    break
                continue
            
            self.stdscr.refresh()
            
            # Control game speed
            time.sleep(0.1)



def main(stdscr):
    game = SnakeGame(stdscr)
    game.run()

if __name__ == "__main__":
    # terminal size
    import os
    rows, cols = os.popen('stty size', 'r').read().split()
    if int(rows) < 10 or int(cols) < 40:
        print("Terminal too small! Please resize to at least 40x10 characters.")
        exit(1)
    
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure your terminal supports color and is large enough.")