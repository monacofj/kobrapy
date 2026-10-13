#!/usr/bin/env python3
#
#   Copyright (c) 2023, Monaco F. J. <monaco@usp.br>
#
#   This file is part of KobraPy.
#
#   KobraPy is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
import sys

import pygame


# Game customization.

WIDTH, HEIGHT = 800, 800  # Game screen dimensions.
GRID_SIZE = 50  # Side length of each grid cell.

HEAD_COLOR = "#00aa00"
DEAD_HEAD_COLOR = "#4b0082"
TAIL_COLOR = "#00ff00"
APPLE_COLOR = "#aa0000"
ARENA_COLOR = "#202020"
GRID_COLOR = "#3c3c3b"
SCORE_COLOR = "#ffffff"
MESSAGE_COLOR = "#808080"

WINDOW_TITLE = "KobraPy"
GAME_SPEED = 7  # Game-loop iterations per second.


# Game implementation.

pygame.init()

clock = pygame.time.Clock()
arena = pygame.display.set_mode((WIDTH, HEIGHT))

BIG_FONT = pygame.font.Font(
    "assets/font/GetVoIP-Grotesque.ttf", int(WIDTH / 8)
)
SMALL_FONT = pygame.font.Font(
    "assets/font/GetVoIP-Grotesque.ttf", int(WIDTH / 20)
)

pygame.display.set_caption(WINDOW_TITLE)

game_on = 1


def center_prompt(title, subtitle):
    """Display a prompt and wait for a key or quit event."""
    center_title = BIG_FONT.render(title, True, MESSAGE_COLOR)
    center_title_rect = center_title.get_rect(
        center=(WIDTH / 2, HEIGHT / 2)
    )
    arena.blit(center_title, center_title_rect)

    center_subtitle = SMALL_FONT.render(subtitle, True, MESSAGE_COLOR)
    center_subtitle_rect = center_subtitle.get_rect(
        center=(WIDTH / 2, HEIGHT * 2 / 3)
    )
    arena.blit(center_subtitle, center_subtitle_rect)

    pygame.display.update()

    # Wait for a key press or a quit event.
    while (event := pygame.event.wait()):
        if event.type == pygame.KEYDOWN:
            break
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()


class Snake:
    """Track the snake's segments, movement, and collisions."""

    def __init__(self):
        self.x, self.y = GRID_SIZE, GRID_SIZE

        # Movement components: -1 (left/up), 0 (still), 1 (right/down).
        self.xmov = 1
        self.ymov = 0

        self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
        self.tail = []
        self.alive = True
        self.got_apple = False

    def update(self):
        """Check collisions, restart if needed, and move the snake."""
        global apple

        # Check for a collision with the arena boundary.
        if (
            self.head.x not in range(0, WIDTH)
            or self.head.y not in range(0, HEIGHT)
        ):
            self.alive = False

        # Check whether the snake has bitten itself.
        for square in self.tail:
            if self.head.x == square.x and self.head.y == square.y:
                self.alive = False

        if not self.alive:
            pygame.draw.rect(arena, DEAD_HEAD_COLOR, snake.head)
            center_prompt("Game Over", "Press to restart")

            # Restore the starting position and direction.
            self.x, self.y = GRID_SIZE, GRID_SIZE
            self.head = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)
            self.tail = []
            self.xmov = 1
            self.ymov = 0
            self.alive = True
            self.got_apple = False

            apple = Apple()

        # Keep the tail in place if the head has not moved.
        if self.xmov or self.ymov:
            self.tail.insert(
                0, pygame.Rect(self.head.x, self.head.y, GRID_SIZE, GRID_SIZE)
            )

            if self.got_apple:
                self.got_apple = False
            else:
                self.tail.pop()

            self.head.x += self.xmov * GRID_SIZE
            self.head.y += self.ymov * GRID_SIZE


class Apple:
    """Represent an apple in the arena."""

    def __init__(self):
        # Choose a random grid position.
        self.x = int(random.randint(0, WIDTH) / GRID_SIZE) * GRID_SIZE
        self.y = int(random.randint(0, HEIGHT) / GRID_SIZE) * GRID_SIZE
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    def update(self):
        """Draw the apple."""
        pygame.draw.rect(arena, APPLE_COLOR, self.rect)


def draw_grid():
    """Draw the arena grid."""
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(arena, GRID_COLOR, rect, 1)


score_rect = BIG_FONT.render("1", True, MESSAGE_COLOR).get_rect(
    center=(WIDTH / 2, HEIGHT / 20 + HEIGHT / 30)
)

draw_grid()

snake = Snake()
apple = Apple()

center_prompt(WINDOW_TITLE, "Press to start")


# Main loop.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ymov = 1
                snake.xmov = 0
            elif event.key == pygame.K_UP:
                snake.ymov = -1
                snake.xmov = 0
            elif event.key == pygame.K_RIGHT:
                snake.ymov = 0
                snake.xmov = 1
            elif event.key == pygame.K_LEFT:
                snake.ymov = 0
                snake.xmov = -1
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_p:
                game_on = not game_on

    # Update the game.
    if game_on:
        snake.update()
        arena.fill(ARENA_COLOR)
        draw_grid()
        apple.update()

    for square in snake.tail:
        pygame.draw.rect(arena, TAIL_COLOR, square)

    pygame.draw.rect(arena, HEAD_COLOR, snake.head)

    # The tail length represents the number of apples collected.
    score = BIG_FONT.render(f"{len(snake.tail)}", True, SCORE_COLOR)
    arena.blit(score, score_rect)

    # Grow the snake and respawn the apple when it is collected.
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.got_apple = True
        apple = Apple()

    pygame.display.update()
    clock.tick(GAME_SPEED)
