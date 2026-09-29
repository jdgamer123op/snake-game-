# Project Report: Tkinter Python Snake Game

## 1. Introduction

This project is a classic **Snake Game** developed using Python’s built-in **Tkinter** library. The objective of the game is to control a snake, eat food to grow, and avoid collisions with walls and itself. The game provides real-time keyboard control, scoring, and increasing difficulty as the snake grows.

The project demonstrates the use of:

* Python GUI programming using Tkinter
* Data structures like `deque`
* Event handling and game loops
* Basic game mechanics and logic

---

## 2. Objectives

The main objectives of this project are:

1. To design a fully functional Snake Game using Python and Tkinter.
2. To implement smooth snake movement using a grid-based system.
3. To increase difficulty progressively as the score increases.
4. To provide clean UI elements like score display and restart option.

---

## 3. System Requirements

### 3.1 Hardware Requirements

* Minimum 2GB RAM
* Any modern processor
* Keyboard for controls

### 3.2 Software Requirements

* Python 3.8 or higher
* Tkinter library (comes pre-installed with Python)
* Any code editor (VS Code, PyCharm, etc.)

---

## 4. Tools & Technologies Used

| Tool/Technology     | Purpose                       |
| ------------------- | ----------------------------- |
| Python              | Main programming language     |
| Tkinter             | GUI and graphics              |
| deque (collections) | Efficient snake body handling |
| Random Module       | Random food generation        |

---

## 5. Game Design

### 5.1 Game Interface

The game window contains:

* Title: "Tkinter Python Snake by Gagandeep Singh Rathore"
* Score display at the top
* 600x600 game canvas
* Restart button

### 5.2 Grid System

The game uses a grid system:

* Grid size: 20x20 pixels
* Total grid: 30 x 30 blocks

This ensures smooth movement and easy position tracking.

---

## 6. Working Principle

The snake moves continuously in one direction. The player uses keyboard arrows / WASD keys to change its direction.

### Controls:

| Key    | Action                    |
| ------ | ------------------------- |
| ↑ or W | Move Up                   |
| ↓ or S | Move Down                 |
| ← or A | Move Left                 |
| → or D | Move Right                |
| R      | Restart (After Game Over) |

Each time the snake eats food:

* Score increases by 1
* Snake body grows
* Game speed increases

---

## 7. Implementation Details

The core implementation includes:

### 7.1 Snake Representation

The snake is implemented using Python’s `deque`:

```python
self.snake = deque([(GRID_WIDTH // 2, GRID_HEIGHT // 2)])
```

This allows efficient addition and removal from both ends of the snake body.

### 7.2 Food Generation

Food spawns randomly and avoids overlapping with the snake:

```python
if new_pos not in self.snake:
    return new_pos
```

### 7.3 Collision Detection

The game ends if:

* Snake hits the wall
* Snake collides with itself

```python
if head_pos in list(self.snake) and head_pos != self.snake[0]:
    return True
```

### 7.4 Game Loop

The game loop runs using Tkinter’s `after()` function:

```python
self.root.after(self.game_speed, self.game_loop)
```

It updates movement and redraws the canvas.

---

## 8. Features of the Game

* Real-time snake movement
* Gradual speed increase
* Score tracking
* Restart functionality
* Clean UI layout

---

## 9. Advantages

* Simple and lightweight
* No external libraries needed
* Beginner friendly
* Easy to modify and extend

---

## 10. Limitations

* No sound effects
* Limited graphics
* Only single-level gameplay

---

## 11. Future Enhancements

Some possible improvements:

* Adding sound effects
* High score system
* More levels and obstacles
* Mobile/touch support
* Theme customization

---

## 12. Conclusion

This Snake Game project successfully demonstrates GUI development using Python Tkinter along with game logic and event handling. It is an excellent beginner-level project that enhances understanding of programming concepts like loops, functions, and object-oriented programming.

---

## 13. Developer Information

**Project Title:** Tkinter Python Snake Game
**Developer:** Gagandeep Singh Rathore
**Technology:** Python, Tkinter
**Year:** 2025