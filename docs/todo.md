To-Do List
==========

Before starting, read [the programming exercise](exercise.md). It explains
how to set up your own project, work collaboratively, document your work,
and plan releases.

Your first development task is to **populate your own repository with GitHub
issues** for the requirements below. Do this before changing the game.
Describe the problem or proposed improvement, the expected result, and how
someone else could verify it. Split larger tasks into smaller issues when
helpful. Do not create these issues in the original KobraPy repository.

For each planned change, use a branch, open a pull request, and discuss and
review it before merging. Fixing the game matters, but practicing an
open-source development workflow is the main purpose of the exercise.

Required Fixes
--------------

Create issues for **all** of these problems and resolve them:

- **Self-collision after reversing direction.** Reversing direction is
  currently allowed, and the snake may bite itself as a consequence.
  However, a collision is not detected correctly when the tail contains
  only one segment. Make collision detection consistent. Your team may
  separately decide whether reverse moves should remain allowed.
- **Apples spawning on the snake.** An apple may appear where the head or
  tail already is. New apples must occupy a free cell.
- **Apples spawning outside the arena.** Sometimes an apple does not appear
  on the visible playing field. Ensure that every apple is placed within
  the playable area.
- **Border and playable-area behavior.** Check what happens when the snake
  reaches the top, bottom, and other edges of the visible arena. The snake
  should not disappear into an invisible row or move beyond the playing
  field before a collision is handled. Make the visible boundaries and
  collision behavior agree.
- **Pausing the game.** Check that pausing freezes *all* gameplay changes,
  including collecting apples or changing the snake's length, until play
  resumes.

Suggested Improvements
----------------------

Choose additional improvements with your team, or propose your own. These
are **ideas, not all mandatory requirements**.

Gameplay and controls:

- **Random starting position.** Place the snake at a valid random location,
  with room to move in its starting direction.
- **Difficulty levels.** Offer easy, normal, and hard settings, or increase
  difficulty as the game progresses.
- **Adjustable speed.** Let the player choose a speed, or make the snake
  faster as it collects apples.
- **Independent movement timing.** Currently the speed of the game loop
  controls both drawing and snake movement. Consider separating movement
  updates from screen refreshes.
- **Alternative controls.** Support WASD in addition to the arrow keys.
- **Multiple or special apples.** Try apples that expire, poison the snake,
  shorten it, or make it grow by more than one segment.

Interface and player experience:

- **Startup menu.** Let players configure options such as name, difficulty,
  grid size, and snake colors.
- **Persistent high score.** Save the best score between game sessions.
- **Clearer on-screen information.** Explain the controls on the start and
  restart screens, and improve the score display.
- **Visual improvements.** Improve the appearance of the snake, apples,
  or arena while keeping the game readable.
- **Sound effects.** Add feedback when an apple is collected or the game
  ends.

You may also suggest different features, provided the team can explain
their value and agree on a manageable scope.

Keep the code welcoming to newcomers: make focused changes and explain
important mechanisms and decisions in clear, human-oriented comments.
