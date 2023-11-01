import pygame
import pygame_gui
from components.const import WIDTH, HEIGHT, SQARE_SIZE, BLACK, CREAM
from components.checkers_window import Checkers
import csv

pygame.init()
pygame.display.set_caption("checkers")
fereastra = pygame.display.set_mode((WIDTH + 100, 700))
background = pygame.Surface((WIDTH + 100, 700))
background.fill(pygame.Color("brown4"))
manager = pygame_gui.UIManager((WIDTH + 100, HEIGHT + 100))
load_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH, 280), (100, 50)),
                                                text="Load Game",
                                                manager=manager)
show_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((HEIGHT, 370), (100, 50)),
                                                text="Show Game",
                                                manager=manager)

def open_file_dialog():
    global file_dialog
    # Pozitie dialog
    rect = pygame.Rect((0, 0), (400, 400))
    rect.center = fereastra.get_rect().center
    # Creare dialog
    file_dialog = pygame_gui.windows.ui_file_dialog.UIFileDialog(rect=rect,
                                                                 manager=manager,
                                                                 allow_picking_directories=False)


def get_row_and_column_from_mouse(position):
    x, y = position
    row = y // SQARE_SIZE
    column = x // SQARE_SIZE

    return row, column

def main():
    checkers = Checkers((-15, -40), manager)
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(60) / 1000
        if checkers.game.is_winner() != None:
            print("Winner:", checkers.game.is_winner())
            break
        elif checkers.game.get_toate_mutarile(checkers.game.tabla, checkers.game.turn) == {}:
            if checkers.game.turn == BLACK:
                print("Winner:", CREAM)
            elif checkers.game.turn == CREAM:
                print("Winner:", BLACK)
            break

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_row_and_column_from_mouse(position)
            if 0 <= row <= 7 and 0 <= column <= 7:
                checkers.game.select(row, column)

            if event.type == pygame.QUIT:
                run = False

            manager.process_events(event)

        manager.update(time_delta)
        fereastra.blit(background, (0, 0))
        manager.draw_ui(fereastra)
        pygame.display.update()

    pygame.quit()

main()