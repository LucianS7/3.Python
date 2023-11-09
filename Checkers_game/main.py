import pygame
from pygame.locals import VIDEORESIZE
from pygame_gui import UIManager, UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton, UIImage
from pygame_gui.core import UIContainer
from components.const import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WIDTH, HEIGHT, BLACK, WHITE
from components.game import Checkers
from components.AI.ai import ai_algorithm


def valid_board_coordinates(position):
    x, y = position
    display_width = pygame.display.Info().current_w
    display_height = pygame.display.Info().current_h
    if (display_width - WIDTH) // 2 < x < (display_width + WIDTH) // 2 \
        and (display_height - HEIGHT) // 2 < y < (display_height + HEIGHT) // 2:
        x_board = x - (display_width - WIDTH) // 2
        y_board = y - (display_height - HEIGHT) // 2 
        return x_board, y_board
    return None


def main():
    pygame.init()

    pygame.display.set_caption("Checkers game window")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_surface.fill(pygame.Color(220, 220, 220))

    manager = UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_window = UIContainer(pygame.Rect(
                            (0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT)),
                            manager=manager,
                            anchors={"center": "center"})

    game_surface = UIImage(pygame.Rect((0, 0),(WIDTH, HEIGHT)),
                                            pygame.Surface((WIDTH, HEIGHT)).convert(),
                                            manager=manager,
                                            container=game_window,
                                            anchors={"center": "center"})
    
    new_game_button = UIButton(
        relative_rect=pygame.Rect((400, 50), (120, 60)),
        text="New Game",
        tool_tip_text="Start a new game",
        container=game_window,
        manager=manager,
        anchors={"center": "center"}
    )

    exit_button = UIButton(
        relative_rect=pygame.Rect((400, -50), (120, 60)),
        text="Exit",
        tool_tip_text="Quit the game",
        manager=manager,
        container=game_window,
        anchors={"center": "center"}
    )

    game = Checkers(game_surface.image)

    font_title = pygame.font.SysFont("arialblack", 40)

    clock = pygame.time.Clock()

    fullscreen_on = False
    running = True
    x = 0
    y = 0
    next_x = 0
    next_y = 0
    move = False
    move_path = []
    ai_color = BLACK
  
    while running:
        time_delta = clock.tick(FPS) / 1000

        game_title = font_title.render("CHECKERS GAME", True, (0, 0, 0))
        game_title_shadow = font_title.render("CHECKERS GAME", True, (128, 128, 128))
        game.draw_captured_pieces(background_surface)
        game.draw_player_turn(background_surface) 
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    fullscreen_on = not fullscreen_on
                    if fullscreen_on:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        background_surface = pygame.Surface((screen.get_width(), screen.get_height()))
                        background_surface.fill(pygame.Color(220, 220, 220))
                        manager.set_window_resolution((screen.get_width(), screen.get_height()))
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)   

            if event.type == VIDEORESIZE:
                new_width, new_height = event.size
                background_surface = pygame.Surface((new_width, new_height))
                background_surface.fill(pygame.Color(220, 220, 220))
                screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
                manager.set_window_resolution((new_width, new_height))
                                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not move:
                    position = pygame.mouse.get_pos()
                    valid_position = valid_board_coordinates(position)
                    if valid_position:
                        row, column = game.get_row_and_column(valid_position)
                        if not game.selected_piece:
                            game.select(row, column)         
                        else:
                            move = game.can_move(row, column)
                            if move:
                                x, y = game.selected_piece.get_position()
                                move_path = game.move_path
                            if not move:
                                game.deselect()

            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    game.reset()

            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    running = False

            if event.type == pygame.QUIT:
                running = False
          
            manager.process_events(event)

        if move:
            if next_x == 0 and next_y == 0:
                next_row, next_column = game.move_path[0]
                next_x, next_y = game.get_center_of_square(next_row, next_column)
            elif x != next_x and next_x !=0:
                x, y = game.render_animation(x, y, next_x, next_y)
            elif x == next_x and next_x != 0:
                del move_path[0]
                if move_path:
                    x = next_x
                    y = next_y
                    next_row, next_column = move_path[0]
                    next_x, next_y = game.get_center_of_square(next_row, next_column)
                else:
                    row, column = game.get_row_and_column((next_x, next_y))
                    game.move(row, column)
                    next_x = 0
                    next_y = 0
                    move = False
        else:
            if game.turn == ai_color:
                value, new_board = ai_algorithm(game.get_board(), 2, ai_color, game)
                if new_board:
                    game.ai_move(new_board)
                    move = True
                    x, y = game.selected_piece.get_position()
                    move_path = game.move_path
                    new_board = None

        screen.blit(background_surface, (0, 0))
        screen.blit(game_title_shadow, (((screen.get_width() - game_title.get_rect().width) // 2 + 2), 7))
        screen.blit(game_title, (((screen.get_width() - game_title.get_rect().width) // 2), 5))

        manager.update(time_delta)
        manager.draw_ui(screen)
        
        game.update(game_surface.image)
        
        if not move and game.has_winner() != None:
            winner = game.has_winner()
            game.show_winner(background_surface, winner)
        elif not move and game.get_all_possible_moves(game.board, game.turn) == {}:
            if game.turn == BLACK:
                game.show_winner(background_surface, WHITE)
            elif game.turn == WHITE:
                game.show_winner(background_surface, BLACK)

    pygame.quit()

main()


