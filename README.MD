# 🕹️ Game Library Manager (ABV) 🎮


## Project Description
A Python-based video game library management system that allows users to maintain a collection of games. Each game in the library contains the following information:

- Name (string)
- Genre (string)
- Price (integer)
- Rating (float 0.0-10.0)
- Availability (boolean)

## Features
The application provides the following functionality:

1. Add new games to the library
2. Search for games by name
3. Edit existing game information
4. Delete games from the library
5. Export game data to text format
6. Import game data from text format
7. View library statistics including:
   - Total number of games
   - Most expensive game
   - Highest rated game
   - Number of available games
   - Games by genre breakdown
8. Display all games in the library

## Project Structure
The project consists of the following files:

- `main.py`: Entry point with menu interface
- `game.py`: Game class definition
- `game_manager.py`: Core game management functionality
- `colors.py`: ANSI color definitions for terminal output

## Requirements
- Python 3.x
- Terminal that supports ANSI color codes

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Run `python main.py`

## Usage
The application presents a user-friendly menu with the following options:

1. Add new game
2. Search game
3. Edit game
4. Delete game
5. Export data
6. Import data
7. Show statistics
8. Show all games
9. Exit

## Data Format
Games are stored in a pipe-separated format:
- name|genre|price|rating|availability

## Color Interface
The application features a colorful terminal interface for better user experience, utilizing:
- Bright cyan for headers
- Yellow for menu options
- Green for success messages
- Red for error messages
- Various colors for data display

## Author
- [@NNKtv28](https://github.com/nnktv28)

## License
MIT License
