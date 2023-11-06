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
    new_x = 0
    new_y = 0
    moving = False
  
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
                if not moving:
                    position = pygame.mouse.get_pos()
                    valid_position = valid_board_coordinates(position)
                    if valid_position:
                        row, column = game.get_row_and_column(valid_position)
                        if not game.selected_piece:
                            game.select(row, column)         
                        else:
                            moving = game.can_move(row, column)
                            if moving:
                                x, y = game.selected_piece.get_position()
                                new_x, new_y = game.get_center_of_square(row, column)
                            else:
                                game.selected_piece.deselect()
                                game.selected_piece = None
                                game.select(row, column)

            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == new_game_button:
                    game.reset()

            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == exit_button:
                    running = False

            if event.type == pygame.QUIT:
                running = False
          
            manager.process_events(event)

        # if game.game.turn == ai_color:
        #     new_board = ai_algorithm(game.get_board(), 2, ai_color, game)
        #     game.ai_move(new_board)

        if moving and x != new_x:
            x, y = game.render_animation(x, y, new_x, new_y)
        if moving and x == new_x and new_x != 0:
            row, column = game.get_row_and_column((new_x, new_y))
            game.move(row, column)
            new_x = 0
            new_y = 0
            moving = False
           
        screen.blit(background_surface, (0, 0))
        screen.blit(game_title_shadow, (((screen.get_width() - game_title.get_rect().width) // 2 + 2), 7))
        screen.blit(game_title, (((screen.get_width() - game_title.get_rect().width) // 2), 5))

        manager.update(time_delta)
        manager.draw_ui(screen)
        
        game.update(game_surface.image)

        if not moving and game.has_winner() != None:
            print("Winner:", game.has_winner())
            pygame.quit()
        elif not moving and game.get_all_possible_moves(game.board, game.turn) == {}:
            if game.turn == BLACK:
                print("Winner: White Player")
            elif game.turn == WHITE:
                print("Winner: Black Player")
            pygame.quit()

    pygame.quit()

main()


