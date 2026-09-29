import tkinter as tk
import random
from collections import deque

GAME_TITLE = "Tkinter Python Snake by Gagandeep Singh Rathore"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = CANVAS_WIDTH // GRID_SIZE
GRID_HEIGHT = CANVAS_HEIGHT // GRID_SIZE
INITIAL_GAME_SPEED = 150

BACKGROUND_COLOR = "#1a1a1a"
SNAKE_COLOR = "#00cc66"
FOOD_COLOR = "#ff3333"
SCORE_COLOR = "#ffffff"
MESSAGE_COLOR = "#ffcc00"

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title(GAME_TITLE)
        self.root.resizable(False, False)

        self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food_pos = self._generate_food()
        self.score = 0
        self.game_over = False
        self.game_speed = INITIAL_GAME_SPEED

        self.score_label = tk.Label(root, text=f"Score: {self.score}",
                                    font=("Helvetica", 18, "bold"), fg=SCORE_COLOR, bg=BACKGROUND_COLOR)
        self.score_label.pack(pady=5)

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

        self.message_label = tk.Label(root, text="", font=("Helvetica", 24, "bold"),
                                      fg=MESSAGE_COLOR, bg=BACKGROUND_COLOR)
        self.message_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart (Press R)", command=self.reset_game,
                                        font=("Helvetica", 14), bg="#333333", fg=SCORE_COLOR, relief=tk.FLAT)
        self.restart_button.pack(pady=5)
        self.restart_button.pack_forget()

        self.root.bind('<Key>', self.on_key_press)

        self.draw_elements()
        self.game_loop()

    def _generate_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            new_pos = (x, y)
            if new_pos not in self.snake:
                return new_pos

    def on_key_press(self, event):
        if event.keysym in ('Up', 'w', 'W'):
            self._set_next_direction((0, -1))
        elif event.keysym in ('Down', 's', 'S'):
            self._set_next_direction((0, 1))
        elif event.keysym in ('Left', 'a', 'A'):
            self._set_next_direction((-1, 0))
        elif event.keysym in ('Right', 'd', 'D'):
            self._set_next_direction((1, 0))
        elif event.keysym in ('r', 'R') and self.game_over:
            self.reset_game()

    def _set_next_direction(self, new_dir):
        current_dx, current_dy = self.direction
        new_dx, new_dy = new_dir
        if (new_dx, new_dy) != (-current_dx, -current_dy):
            self.next_direction = new_dir

    def move_snake(self):
        if self.game_over:
            return

        self.direction = self.next_direction
        dx, dy = self.direction
        head_x, head_y = self.snake[0]
        new_head = (head_x + dx, head_y + dy)

        if self._check_collision(new_head):
            self.end_game()
            return

        self.snake.appendleft(new_head)

        if new_head == self.food_pos:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food_pos = self._generate_food()

            self.game_speed = max(50, self.game_speed - 2)
        else:
            self.snake.pop()

    def _check_collision(self, head_pos):
        x, y = head_pos
        if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            return True
        if head_pos in list(self.snake) and head_pos != self.snake[0]:
             return True
        return False

    def draw_elements(self):
        self.canvas.delete(tk.ALL)

        for x, y in self.snake:
            x1 = x * GRID_SIZE
            y1 = y * GRID_SIZE
            x2 = x1 + GRID_SIZE
            y2 = y1 + GRID_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=SNAKE_COLOR, outline=BACKGROUND_COLOR)

        fx, fy = self.food_pos
        x1 = fx * GRID_SIZE
        y1 = fy * GRID_SIZE
        x2 = x1 + GRID_SIZE
        y2 = y1 + GRID_SIZE
        pad = 3
        self.canvas.create_oval(x1 + pad, y1 + pad, x2 - pad, y2 - pad, fill=FOOD_COLOR)

        hx, hy = self.snake[0]
        self.canvas.create_rectangle(hx*GRID_SIZE, hy*GRID_SIZE,
                                     (hx+1)*GRID_SIZE, (hy+1)*GRID_SIZE,
                                     fill=SNAKE_COLOR, outline=SCORE_COLOR, width=2)

    def game_loop(self):
        if not self.game_over:
            self.move_snake()
            self.draw_elements()

        self.root.after(self.game_speed, self.game_loop)

    def end_game(self):
        self.game_over = True
        self.message_label.config(text=f"GAME OVER! Final Score: {self.score}", fg=MESSAGE_COLOR)
        self.restart_button.pack(pady=10)

    def reset_game(self):
        self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food_pos = self._generate_food()
        self.score = 0
        self.game_over = False
        self.game_speed = INITIAL_GAME_SPEED

        self.score_label.config(text=f"Score: {self.score}")
        self.message_label.config(text="")
        self.restart_button.pack_forget()

        self.draw_elements()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()