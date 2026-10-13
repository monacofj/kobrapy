KobraPy Manual
==============

KobraPy is a simple Python implementation of the classic snake game.

Requirements
------------

- Python 3
- Pygame (https://www.pygame.org)

Install Pygame, if needed, with:

```sh
pip install pygame
```

Running the Game
----------------

- Linux/macOS: `./kobra.py`
- Windows: `python kobra.py`

The Game
--------

Guide a snake through a rectangular arena, collecting apples that appear at
random positions. Each apple increases your score and makes the snake grow
longer.

But beware! The arena borders are electrified, and the snake is poisonous to
itself. Hitting a wall or biting its own tail ends the game.

The goal is simple: eat as many apples as you can.

Controls
--------

- **Arrow keys:** Steer the snake.
- **P:** Pause or resume the game.
- **Q:** Quit the game.

Press any key to start. After a game over, press any key to play again, or
`Q` to quit.

Programming Exercise
--------------------

For instructions on using KobraPy as a programming exercise, see
[`docs/exercise.md`](exercise.md).
