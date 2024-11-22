from game_manager import GameManager
from colors import BRIGHT_GREEN, CYAN, RESET, BRIGHT_RED, BRIGHT_CYAN, YELLOW, GREEN, RED,BRIGHT_BLUE
import sys

def display_menu():
    print(f"\n{BRIGHT_CYAN}=== ADMINISTRADOR DE BIBLIOTECA DE VIDEOJUEGOS (ABV) ==={RESET}")
    print(f"{YELLOW}1. Agregar nuevo juego")
    print("2. Buscar juego")
    print("3. Editar juego")
    print("4. Eliminar juego")
    print("5. Exportar datos a texto")
    print("6. Importar datos desde texto")
    print("7. Mostrar estadisticas")
    print("8. Mostrar todos los juegos")
    print(f"9. Salir{RESET}") # RESET de colores

def main():
    game_manager = GameManager()
    
    while True:
        display_menu()
        choice = input(f"\n{GREEN}Seleccione una opcion (1-9): {RESET}")
        
        if choice == "1":
            game_manager.add_game()
        elif choice == "2":
            game_id = input(f"{CYAN}Ingrese ID del juego: {RESET}")
            game_manager.search_game(game_id)
        elif choice == "3":
            game_id = input(f"{CYAN}Ingrese ID del juego a editar: {RESET}")
            game_manager.edit_game(game_id)
        elif choice == "4":
            game_id = input(f"{RED}Ingrese ID del juego a eliminar: {RESET}")
            game_manager.delete_game(game_id)
        elif choice == "5":
            exported_data = game_manager.export_data()
            print(f"\n{BRIGHT_BLUE}Datos exportados: {RESET}{exported_data}")
        elif choice == "6":
            #data = input(f"{CYAN}Ingrese el texto de datos a importar: {RESET}")
            data = """1|ark|shooter|50|10.0|True 
            2|alskjd|laskjd|39|10.0|False
            2|alskjd|laskjd|39|10.0|False
            3|ARK|shooter|34|4.0|True
            5|ark|shooter|49|10.0|True"""
            game_manager.import_data(data)
        elif choice == "7":
            game_manager.show_statistics()
        elif choice == "8":
            game_manager.display_all_games()
        elif choice == "9":
            print(f"\n{BRIGHT_GREEN}Gracias por usar ABV!{RESET}")
            sys.exit(0)
        else:
            print(f"\n{BRIGHT_RED}Opcion invalida. Por favor intente de nuevo.{RESET}")

if __name__ == "__main__":
    main()