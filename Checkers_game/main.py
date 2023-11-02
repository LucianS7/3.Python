import pygame
import pygame_gui
from components.const import WIDTH, HEIGHT, SQUARE_SIZE, BLACK, CREAM
from components.checkers_window import Checkers
import csv

pygame.init()
pygame.display.set_caption("checkers")
window = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
background_surface = pygame.Surface((WIDTH + 100 , HEIGHT + 100))
background_surface.fill(pygame.Color(200, 200, 200))
manager = pygame_gui.UIManager((WIDTH + 100, HEIGHT + 100))
new_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(((WIDTH  // 2) -10 , HEIGHT + 20), (120, 60)),
                                                text="New Game",
                                                manager=manager)


def get_row_and_column_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    column = (x - 45) // SQUARE_SIZE

    return row, column


def main():
    checkers = Checkers((30,-40), manager)
    clock = pygame.time.Clock()
    run = True
    while run:
        time_delta = clock.tick(60) / 1000
        if checkers.game.has_won() != None:
            print("Winner:", checkers.game.has_won())
            break
        elif checkers.game.get_all_possible_moves(checkers.game.board, checkers.game.turn) == {}:
            if checkers.game.turn == BLACK:
                print("Winner: White Player")
            elif checkers.game.turn == CREAM:
                print("Winner: Black Player")
            break

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, column = get_row_and_column_from_mouse(position)
                if 0 <= row <= 7 and 0 <= column <= 7:
                    checkers.game.select(row, column)
                    
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    checkers.game.reset()

            if event.type == pygame.QUIT:
                run = False

            manager.process_events(event)

        manager.update(time_delta)
        window.blit(background_surface, (0, 0))
        manager.draw_ui(window)
        pygame.display.update()

    pygame.quit()

main()