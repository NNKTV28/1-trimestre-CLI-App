# 🕹️ Game Library Manager (ABV) 🎮

## Project Description
A Python-based video game library management system with colored terminal interface that allows users to maintain a collection of games. Each game entry contains:

- Name (unique identifier)
- Genre (string)
- Price (integer/float)
- Rating (float 0.0-10.0)
- Availability (boolean)

## Features
The application provides:

1. Add new games with duplicate name checking
2. Search for games by exact name match
3. Edit existing game details with validation
4. Delete games from the library
5. Export game data to pipe-separated format
6. Import game data with error handling and type validation
7. View comprehensive library statistics:
   - Total game count
   - Most expensive game
   - Highest rated game
   - Available games count
   - Genre distribution
8. Display all games sorted alphabetically

## Project Structure
- `main.py`: Menu interface and program entry point
- `game.py`: Game class with core attributes
- `game_manager.py`: Game collection management and operations
- `colors.py`: ANSI color constants for terminal styling

## Technical Requirements
- Python 3.x
- Terminal with ANSI color support
- No external dependencies required

## Data Format
Games are stored in pipe-separated format:
   name|genre|price|rating|available
### Example:
- The Legend of Zelda: Breath of the Wild|Action-Adventure|60|9.8|true

## Color Scheme
- BRIGHT_CYAN: Headers and menus
- YELLOW: Menu options and secondary information
- BRIGHT_GREEN: Success messages
- BRIGHT_RED: Error messages and warnings
- BRIGHT_WHITE/BRIGHT_CYAN: Game information display
- BRIGHT_MAGENTA: Section titles

## Installation & Usage
1. Clone the repository
2. Navigate to project directory
3. Run:
```bash
python main.py
```
## Author
@NNKtv28 - https://github.com/NNKtv28

## License
MIT License