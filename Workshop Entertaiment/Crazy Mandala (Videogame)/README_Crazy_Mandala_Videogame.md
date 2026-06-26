# Crazy Mandala (Videogame)

> Learning videogame project — Assisted with AI Codex created for fun and practice in Stanford Code in Place.

**Crazy Mandala** is an interactive Python canvas game where the player scratches a colorful mandala-style lion image and unlocks different mini-game phases as progress increases.

Project link: https://codeinplace.stanford.edu/cip6/share/TVo5R6JhkT2BpsAXomxB

## What it does

The game starts by asking for a player name in the terminal. Then the player interacts with the canvas to reveal the hidden mandala lion and reach 100% progress.

The experience changes as the player advances:

- Scratch the mandala using a machete-style cursor.
- Reveal colorful lion artwork hidden under the cover layer.
- Unlock a bouncing ball challenge.
- Unlock a double-ball challenge.
- Unlock a snake-style final level.
- Win by reaching 100% progress.
- Save player scores locally using a JSON file.

## Main Features

- Interactive graphics using `graphics.Canvas`
- Player name prompt
- Local player profile tracking
- Score and attempt system
- Colorful mandala lion artwork
- Scratch-to-reveal gameplay
- Progress bar
- Level transitions
- Bouncing ball mini-game
- Double-ball mini-game
- Snake final level
- Restart button
- Lion facts during the game

## Stack

- Python 3
- `graphics.py` / `graphics.Canvas`
- `math`
- `os`
- `random`
- `time`

## Project Structure

```text
Crazy Mandala (Videogame)/
├── main.py
├── machete.png
└── README_Crazy_Mandala_Videogame.md
```

## How to Run

```bash
python main.py
```

The game needs the Code in Place graphics environment or a compatible `graphics.py` setup.

## Gameplay Flow

```text
Player enters name
    -> Scratch mandala area
    -> Reach 40% progress
    -> Bouncing ball challenge starts
    -> Reach 60% progress
    -> Double-ball challenge starts
    -> Reach 80% progress
    -> Snake level starts
    -> Reach 100% progress
    -> Win screen appears
```

## Game Phases

### Scratch Phase

The player grabs the machete cursor and moves it across the mandala area. Scratching reveals parts of the hidden lion artwork.

### Bounce Phase

At 40% progress, the game changes into a bouncing ball challenge. The player uses a bamboo paddle to keep the ball alive and continue revealing the mandala.

### Double Bounce Phase

At 60% progress, two balls appear. The player must keep the game going while both balls reveal more of the hidden image.

### Snake Phase

At 80% progress, the game becomes a snake-style challenge. The player guides the snake while avoiding the red worm.

### Win Phase

At 100%, the player wins and the game records the score.

## Player Profiles

The game creates player profiles with IDs like:

```text
CM-001
```

It stores:

- Player name
- Player ID
- Best score
- Best attempt
- Number of plays

## Why this project is interesting

This project is more than a simple drawing. It combines:

- Canvas graphics
- Game state management
- Multiple game phases
- Mouse interaction
- Restart logic
- Visual feedback

It is a good example of how Python can be used to create an interactive entertainment project.

## Future Improvements

Possible future improvements:

- Add sound effects
- Add a start menu
- Add difficulty levels
- Add more animal mandalas
- Add mobile-friendly controls
- Add a leaderboard screen
- Add better animations
- Add collectible items
- Improve collision detection
- Add instructions inside the canvas
- Storage for best score players

## Status

Active learning project. The game logic, graphics, and interaction flow may still be improved.

## Disclaimer

This is a learning videogame project. It is not intended for production release.

## Author

Created by **Bryan Bodegas** as a Stanford Code in Place entertainment project.

## One-sentence summary

Crazy Mandala is a Python canvas videogame where the player reveals a colorful mandala lion through scratch, bounce, and snake-style mini-game phases.