To-Do List
==========

Before you begin, read [the programming exercise](exercise.md). It explains
how to set up your own project, document your work, collaborate, and plan
releases.

Start by populating **your own repository** with GitHub issues for the
requirements below. Do this **before implementing changes**: each issue should
describe a problem or feature, explain the expected behavior, and provide
enough context for a teammate to work on it. You may split large tasks into
smaller issues.

Then plan the work with your team. For each issue, create a branch, submit a
pull request, and review the changes before merging. The goal is to practice
open-source collaboration, not just to finish the game.

Required Fixes
--------------

Create issues for and resolve **all** of the following bugs:

- **Self-collision after reversing direction.** Reversing direction is
  currently allowed and can cause the snake to bite itself. However, the
  collision is not detected correctly when the tail has only one segment.
  Make collision detection consistent.
- **Apples appearing on the snake.** An apple can be placed on a cell
  already occupied by the snake. Ensure that new apples appear in an
  available location.
- **Apples appearing outside the arena.** Occasionally an apple is placed
  beyond the visible playing area. Apples must remain inside the arena.

Suggested Improvements
----------------------

Create issues for the improvements your team chooses to implement. You may
also propose your own ideas.

- **Random starting position.** Start the snake at a random valid position,
  with enough space to move in its initial direction.
- **Startup menu.** Let players configure options before starting a game,
  such as their name, grid size, or difficulty.
- **Difficulty levels.** Offer presets (for example, easy, normal, and hard)
  or let the difficulty increase as the game progresses.
- **High score.** Record the best score and preserve it between game
  sessions.
- **More game options.** Consider varying the snake's speed, allowing
  multiple apples, introducing apples that expire, or adding special
  apples with different effects.

Keep the project understandable for newcomers. Prefer focused changes and
clear explanations of what was changed and why.

Remember: this is a starting point for **your project's issue tracker**,
not a checklist to complete directly in the KobraPy repository.
