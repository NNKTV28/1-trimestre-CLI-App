from game import Game
from colors import BRIGHT_GREEN, CYAN, RESET, BRIGHT_RED, BRIGHT_MAGENTA, BRIGHT_WHITE, BRIGHT_CYAN, YELLOW,BRIGHT_YELLOW
class GameManager:
    def __init__(self):
        self.games = []
        
    def return_no_games(self):
        print(f"\n{BRIGHT_RED}<-- No hay juegos registrados -->{RESET}")

    def add_game(self):
        name = input(f"{CYAN}Ingrese el nombre del juego: {RESET}")
        if self._find_game(name):
            print(f"\n{BRIGHT_RED}Error: ¡Ya existe un juego con este nombre!{RESET}")
            return

        genre = input(f"{CYAN}Ingrese el género del juego: {RESET}")
        price = int(input(f"{CYAN}Ingrese el precio del juego (número entero): {RESET}"))
        rating = float(input(f"{CYAN}Ingrese la calificación del juego (0.0-10.0): {RESET}"))
        available = input(f"{CYAN}¿Está disponible el juego? (si/no): {RESET}").lower() == 'si'

        game = Game(name, genre, price, rating, available)
        self.games.append(game)
        print(f"\n{BRIGHT_GREEN}¡Juego agregado exitosamente!{RESET}")

    def search_game(self, name):
        game = self._find_game(name)
        if game:
            self._display_game(game)
        else:
            print(f"\n{BRIGHT_RED}¡Juego no encontrado!{RESET}")

    def edit_game(self, name):
        game = self._find_game(name)
        if not game:
            print(f"\n{BRIGHT_RED}¡Juego no encontrado!{RESET}")
            return

        new_name = input(f"{CYAN}Ingrese nuevo nombre: {RESET}")
        if new_name != name and self._find_game(new_name):
            print(f"\n{BRIGHT_RED}Error: ¡Ya existe un juego con este nombre!{RESET}")
            return
        game.name = new_name
        game.genre = input(f"{CYAN}Ingrese nuevo género: {RESET}")
        game.price = int(input(f"{CYAN}Ingrese nuevo precio: {RESET}"))
        game.rating = float(input(f"{CYAN}Ingrese nueva calificación: {RESET}"))
        game.available = input(f"{CYAN}¿Está disponible el juego? (si/no): {RESET}").lower() == 'si'
        print(f"\n{BRIGHT_GREEN}¡Juego actualizado exitosamente!{RESET}")

    def delete_game(self, name):
        game = self._find_game(name)
        if game:
            self.games.remove(game)
            print(f"\n{BRIGHT_GREEN}¡Juego eliminado exitosamente!{RESET}")
        else:
            print(f"\n{BRIGHT_RED}¡Juego no encontrado!{RESET}")

    def show_statistics(self):
        if not self.games:
            print(f"\n{YELLOW}¡No hay juegos en la biblioteca!{RESET}")
            return

        print(f"\n{BRIGHT_MAGENTA}=== ESTADÍSTICAS DE LA BIBLIOTECA ==={RESET}")
        print(f"{BRIGHT_CYAN}Total de juegos: {len(self.games)}")
        print(f"Juego más caro: {max(self.games, key=lambda x: x.price).name}")
        print(f"Juego mejor calificado: {max(self.games, key=lambda x: x.rating).name}")
        print(f"Juegos disponibles: {sum(1 for game in self.games if game.available)}{RESET}")
        print(f"\n{BRIGHT_YELLOW}Juegos por género:{RESET}")
        genres = {}
        for game in self.games:
            genres[game.genre] = genres.get(game.genre, 0) + 1
        for genre, count in sorted(genres.items()):
            print(f"{YELLOW}- {genre}: {count}{RESET}")

    def display_all_games(self):
        if not self.games:
            self.return_no_games()
            return
        
        print(f"\n{BRIGHT_MAGENTA}<=== TODOS LOS JUEGOS ===>{RESET}")
        for game in sorted(self.games, key=lambda x: x.name):
            self._display_game(game)

    def _display_game(self, game):
        print(f"\n{BRIGHT_WHITE}Nombre: {BRIGHT_CYAN}{game.name}")
        print(f"{BRIGHT_WHITE}Genero: {BRIGHT_CYAN}{game.genre}")
        print(f"{BRIGHT_WHITE}Precio: ${BRIGHT_CYAN}{game.price}")
        print(f"{BRIGHT_WHITE}Calificacion: {BRIGHT_CYAN}{game.rating:.1f}/10.0")
        print(f"{BRIGHT_WHITE}Disponible: {BRIGHT_GREEN if game.available else BRIGHT_RED}{'Sí' if game.available else 'No'}{RESET}")
        
    def _find_game(self, name):
        for game in self.games:
            if game.name == name:
                return game
        return None

    def export_data(self):
        return "\n".join(str(game) for game in self.games)

    def import_data(self, data):
        if not data.strip():
            return
        for line in data.split('\n'):
            if line.strip():
                name, genre, price, rating, available = line.split('|')
                game = Game(name, genre, int(price), float(rating), available.lower() == 'true')
                self.games.append(game)