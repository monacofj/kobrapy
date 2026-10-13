KobraPy Manual
==============

KobraPy is a simple Python implementation of the classic snake game.

Requirements
------------

- Python 3
- Pygame (https://www.pygame.org)

Setup and Running
-----------------

Run the following commands from the KobraPy project directory. A virtual
environment keeps Pygame separate from other Python projects and from your
system Python installation.

On Linux/macOS:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame
python kobra.py
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\\Scripts\\Activate.ps1
python -m pip install pygame
python kobra.py
```

When returning to the project in a new terminal, activate the existing
environment again; you do not need to reinstall Pygame. The `.venv`
directory is excluded from version control.

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
