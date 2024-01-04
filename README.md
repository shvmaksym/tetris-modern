# Tetris Modern Clone

Tetris Modern Clone is a modern implementation of the classic Tetris game in Python, utilizing the Pygame library.

## Video Demo: https://youtu.be/w8uZSJlrIao

## Description

In this version of Tetris Modern, two additional shapes have been introduced compared to the classic Tetris, making the game even more diverse and intriguing for players. The new shapes bring unique block placements and gameplay strategies, adding extra challenges for Tetris enthusiasts and infusing fresh elements into the traditional gameplay. Players will have the opportunity to stand out in their experience and skills by maneuvering with these new shapes to achieve the best results. The inclusion of these novel figures enhances the overall Tetris experience, providing an exciting twist for those familiar with the classic game.

## Technical Details

### Code Structure

The game code is organized into several files:

- **project.py:** Entry point of the game, initializes Pygame, and handles the game loop.
- **run_game.py:** Contains the `Run` class, managing the game state, including the grid, blocks, score, and level.
- **grid.py:** Defines the `Grid` class, responsible for managing the game grid and handling block placement.
- **blocks.py:** Defines different block shapes, each with its own movement and rotation logic.

### Game Logic

- The game starts with an initialized grid and a random selection of blocks.
- Blocks are randomly shuffled, and the current and next blocks are set accordingly.
- The game loop handles user input, block movements, rotations, and collision detection.
- The game speeds up as the player scores more points, with increasing difficulty levels.
- Scoring is based on the number of lines cleared, providing additional points for multiple lines simultaneously.

### Running the Game

1. Ensure you have Python and Pygame installed (`pip install pygame`).
2. Run the game by executing `project.py`.
3. Use arrow keys for block movement and rotation, 'P' to pause, and 'Enter' to start/restart the game.
4. To use the tests, you need to install the pytest (`pip install pytest`)

## Setup Instructions

1. Open a terminal or command prompt and navigate to the project folder using the `cd /path_to_project_folder` command.
2. To install pygame using the following command:

    ```bash
    pip install pygame
    ```

3. To install pytest:

    ```bash
    pip install pytest
    ```

## Acknowledgments

This project is built with the Pygame library. Special thanks to the Pygame community for their contributions to game development in Python.
