# A great Sunday!

> Learning entertainment project — created with Python and AI assistance for Stanford Code in Place.

**A great Sunday!** is a bilingual Python canvas app that helps users decide what to do on a free Sunday. The app lets the user choose a recommendation bot, answer five quick questions, and receive a practical suggestion based on their preferences.

Project link: https://codeinplace.stanford.edu/cip6/ide/p/Ztg03U6I1xXUaHIeXTOo

## What it does

The app offers six Sunday assistants:

- Movie Bot
- Series & Cartoons Bot
- Music Bot
- Book Bot
- Game Bot
- Cooking Bot

Each assistant asks five short questions in the terminal and shows the experience visually on the canvas.

## Key Features

- English and Spanish language selection
- Visual menu with six assistant cards
- Terminal-based answers
- Five-question decision flow
- Canvas screens for selection, questions, loading, and results
- Optional AI-assisted recommendations when supported by the environment
- Safe fallback response when AI assistance is not available
- Simple icons and image support for each bot
- Restart option after the recommendation

## Stack

- Python 3
- Code in Place canvas graphics library
- `time`
- Optional AI helper available in some Code in Place environments
- Image files for bot cards, such as `Movies.png`, `Series.png`, `music.png`, `Books.png`, `Game.png`, and `Food.png`

## How to Run

```bash
python main.py
```

The project is designed for the Stanford Code in Place environment or a compatible Python graphics setup.

## App Flow

```text
Choose language
    -> Choose Sunday assistant
    -> Type your name
    -> Answer 5 questions
    -> Generate recommendation
    -> Review result on canvas
    -> Restart or finish
```

## Why this project is useful

This project combines entertainment, user input, bilingual interface design, AI-assisted recommendations, and safe fallback logic. It is a simple but practical example of how a Python app can guide a user through a personalized decision process.

## Status

Active learning project. The interface, recommendations, and visual design may continue improving.

## Disclaimer

This is an educational project. AI-generated suggestions should always be reviewed before making decisions.

## Author

Created by **Bryan Bodegas** as a Stanford Code in Place entertainment project.

## One-sentence summary

A great Sunday! is a bilingual Python recommendation app that helps users choose movies, series, music, books, games, or cooking ideas for a better day off.
