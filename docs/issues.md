Issue Catalog
=============

This catalog lists small, reviewable contributions to the KobraPy programming
exercise. Each row is a suggested GitHub issue for the **student's own project**,
not an issue to open in the original KobraPy repository.

The **ID** is a stable catalog reference, **not** a GitHub issue number.
Use it when recording dependencies; your repository's GitHub issue numbers
will be different.

**Priority** describes the exercise requirement:

- **Critical:** a known defect that every team must fix.
- **Required:** a mandatory feature or repository-maintenance task.
- **Wish:** an optional contribution that students may choose.

The **Difficulty** estimates the scope for a beginner: Easy, Moderate, or
Advanced. **Depends on** lists catalog IDs that should be completed first;
a dash means no known prerequisite. Dependencies describe the planned exercise,
not necessarily every technically possible implementation. Other conflicts
may still arise when contributors edit the same source file.

The configuration panel (#07) is deliberately a single initial task. Features
that require player-selectable options depend on it and include their own
integration into the panel. There are no predefined difficulty levels.

| ID | Title | Description | Priority | Difficulty | Depends on |
| --- | --- | --- | --- | --- | --- |
| 01 | Self-collision after reversal | Detect self-collision correctly, including when the tail has one segment. | Critical | Moderate | — |
| 02 | Apples spawning on snake | Spawn apples only on cells not occupied by the snake. | Critical | Easy | — |
| 03 | Apples spawning outside arena | Keep every apple within the visible playable area. | Critical | Easy | — |
| 04 | Arena boundaries | Make visible boundaries and wall-collision behavior agree. | Critical | Moderate | — |
| 05 | Pause behavior | Freeze all game-state changes while the game is paused. | Critical | Easy | — |
| 06 | Asset loading | Load font assets regardless of the current working directory. | Critical | Easy | — |
| 07 | Configuration panel | Provide a keyboard-operated options panel, initially supporting snake speed. | Required | Moderate | — |
| 08 | Random starting position | Start the snake in a random valid position with room to move. | Wish | Moderate | — |
| 09 | Random initial direction | Choose a valid initial movement direction at random. | Wish | Easy | — |
| 10 | Progressive speed | Optionally increase snake speed as apples are collected. | Wish | Easy | 07 |
| 11 | Poisoned apples | Add an optional apple type that ends the game when collected. | Wish | Moderate | 07 |
| 12 | Disappearing apples | Optionally expire uneaten apples after a timeout and replace them. | Wish | Moderate | 07 |
| 13 | Blinking apples | Make expiring apples blink shortly before disappearing. | Wish | Easy | 12 |
| 14 | Bonus apples | Add an optional apple type worth extra points. | Wish | Moderate | 07 |
| 15 | Extra-growth apples | Add an optional apple type that grows the snake by two segments. | Wish | Moderate | 07 |
| 16 | Shrinking apples | Add an optional apple type that shortens the snake safely. | Wish | Moderate | 07 |
| 17 | Multiple apples | Allow an optional setting for several apples at once without overlapping occupied cells. | Wish | Moderate | 02, 03, 07 |
| 18 | Arena obstacles | Add optional obstacles that the snake must avoid. | Wish | Moderate | 07 |
| 19 | Wrap-around movement | Optionally let the snake emerge at the opposite edge of the arena. | Wish | Moderate | 04, 07 |
| 20 | Inverted controls | Offer an optional mode in which directional controls are reversed. | Wish | Easy | 07 |
| 21 | Initial snake length | Let players choose a longer starting snake in the options panel. | Wish | Easy | 07 |
| 22 | WASD controls | Support WASD movement alongside the arrow keys. | Wish | Easy | — |
| 23 | Space to pause | Use Space to pause and resume the game. | Wish | Easy | 05 |
| 24 | Escape to quit | Let players leave the game with Escape. | Wish | Easy | — |
| 25 | Restart shortcut | Let players restart a game using R. | Wish | Moderate | — |
| 26 | Grid visibility | Use G to show or hide the background grid. | Wish | Easy | — |
| 27 | Final score | Show the final score on the Game Over screen. | Wish | Easy | — |
| 28 | Cause of death | Distinguish wall collisions from self-collisions on Game Over. | Wish | Moderate | — |
| 29 | Pause indicator | Display a clear message while the game is paused. | Wish | Easy | 05 |
| 30 | Controls on start screen | Show the basic keyboard controls before the game begins. | Wish | Easy | — |
| 31 | Speed display | Show the snake's current speed during play. | Wish | Easy | — |
| 32 | Games played | Count how many games have finished during the current session. | Wish | Easy | — |
| 33 | Session high score | Track the best score until the program exits. | Wish | Easy | — |
| 34 | Persistent high score | Save and restore the high score across program runs. | Wish | Moderate | 33 |
| 35 | Elapsed game time | Display elapsed play time without counting paused time. | Wish | Moderate | 05 |
| 36 | Screenshot shortcut | Save a screenshot of the game when F12 is pressed. | Wish | Easy | — |
| 37 | Start countdown | Show a short countdown before gameplay begins. | Wish | Moderate | — |
| 38 | Apple sound | Play a sound when the snake collects an apple. | Wish | Easy | — |
| 39 | Game-over sound | Play a sound when the snake dies. | Wish | Easy | — |
| 40 | Victory condition | Declare victory when the snake occupies every playable cell. | Wish | Moderate | 02, 03 |
| 41 | Cache background grid | Reuse a rendered grid rather than drawing all grid lines every frame. | Wish | Moderate | — |
| 42 | Cache score text | Render score text again only when the displayed value changes. | Wish | Easy | — |
| 43 | Rename Apple.update() | Rename the apple drawing method to describe what it actually does. | Wish | Easy | — |
| 44 | Extract quit function | Centralize repeated game-exit code in a small helper function. | Wish | Easy | — |
| 45 | Remove redundant position | Keep a single authoritative representation of snake-head coordinates. | Wish | Moderate | — |
| 46 | Extract snake reset | Move snake reinitialization into a dedicated method. | Wish | Moderate | — |
| 47 | Boolean pause state | Replace the numeric play/pause flag with a clear Boolean variable. | Wish | Easy | — |
| 48 | Independent movement timing | Separate snake movement updates from the screen refresh rate. | Wish | Advanced | — |
| 49 | Grid configuration validation | Validate that arena dimensions are compatible with the grid size. | Wish | Easy | — |
| 50 | REUSE compliance | Adopt SPDX and REUSE licensing metadata; preserve attribution and pass reuse lint. | Required | Moderate | — |
| 51 | Issue templates | Provide GitHub templates for bug reports and feature requests. | Required | Easy | — |
| 52 | Repository labels | Use the MoeaBench labels bug, feat, chore, wish, and noplan. | Required | Easy | — |
| 53 | Dependency management | Record dependencies in requirements.txt and document virtual-environment setup. | Required | Easy | — |
| 54 | Project documentation | Update AUTHORS, README.md, CONTRIBUTING.md, and docs/conventions.md for the new project. | Required | Moderate | — |
| 55 | Command-line speed | Allow setting an initial speed with a --speed argument. | Wish | Easy | — |
| 56 | Font fallback | Use a default font when the bundled font cannot be loaded. | Wish | Easy | 06 |
| 57 | In-game help | Show or hide a brief controls reference with H. | Wish | Moderate | — |
| 58 | Direction indicator | Display the snake's current movement direction. | Wish | Easy | — |
| 59 | Apples collected counter | Count apples collected in the current game. | Wish | Easy | — |
| 60 | Previous game score | Show the previous game's score on the next start screen. | Wish | Easy | — |
| 61 | New record notification | Notify the player when the session high score is beaten. | Wish | Easy | 33 |
| 62 | Longest snake | Track the greatest snake length reached during the session. | Wish | Easy | — |
| 63 | Toggle HUD | Add a shortcut to hide or show gameplay information. | Wish | Easy | — |
| 64 | Final game duration | Show the total play time on Game Over. | Wish | Easy | 35 |
| 65 | Reverse movement option | Let players forbid immediate reversals using the options panel. | Wish | Easy | 01, 07 |
| 66 | Temporary speed boost | Increase movement speed while Shift is held. | Wish | Moderate | — |
| 67 | Apple expiration indicator | Show the time remaining before an apple expires. | Wish | Moderate | 12 |
| 68 | Configurable apple timeout | Allow players to set the expiration time of disappearing apples. | Wish | Easy | 07, 12 |
| 69 | Configurable obstacle count | Allow players to choose how many obstacles appear. | Wish | Easy | 07, 18 |
| 70 | Mute shortcut | Toggle enabled sound effects using M. | Wish | Easy | 38 |
| 71 | Sound volume | Provide keyboard controls for the volume of sound effects. | Wish | Easy | 38 |
| 72 | Restore default settings | Add a way to restore the options panel's default values. | Wish | Easy | 07 |
| 73 | Remember game settings | Save and restore selected options using a JSON file. | Wish | Moderate | 07 |
| 74 | Configuration summary | Show the selected settings before the game starts. | Wish | Easy | 07 |
| 75 | Numeric keypad controls | Support movement using the numeric keypad. | Wish | Easy | — |
| 76 | Reproducible random seed | Accept a --seed argument for repeatable random sequences. | Wish | Moderate | — |
| 77 | Game history | Append completed game results to a CSV file. | Wish | Moderate | — |
| 78 | Debug overlay | Toggle a view of coordinates and frames per second. | Wish | Easy | — |
| 79 | Extract apple spawning | Move apple-position selection into a named helper function. | Wish | Easy | 02, 03 |
| 80 | Extract score rendering | Move score-drawing code into a small dedicated function. | Wish | Easy | — |
| 81 | Screenshot directory | Save game screenshots in a dedicated output directory. | Wish | Easy | 36 |
| 82 | Screenshot confirmation | Briefly indicate when a screenshot has been saved. | Wish | Easy | 36 |
| 83 | Top five high scores | Maintain and display the five highest saved scores. | Wish | Moderate | 34 |

Students should turn selected catalog entries into actionable issues with
their own acceptance criteria and verification steps. Prefer small pull
requests that preserve the game's behavior outside the intended change.
