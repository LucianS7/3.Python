import pygame
from pygame_gui.elements.ui_window import UIWindow
from pygame_gui.elements.ui_image import UIImage
from components.game import Game
from components.const import WIDTH, HEIGHT

class Checkers(UIWindow):

    def __init__(self, pozitie, ui_manager):
        super().__init__(pygame.Rect(pozitie, (WIDTH + 32, HEIGHT + 59)), ui_manager,
                         window_display_title="",
                         object_id="#checkers_window")
        game_surface_size = self.get_container().get_size()
        self.game_surface_element = UIImage(pygame.Rect((0, 0),
                                                        game_surface_size),
                                            pygame.Surface(game_surface_size).convert(),
                                            manager=ui_manager,
                                            container=self,
                                            parent_element=self)
        self.game = Game(self.game_surface_element.image)

    def update(self, time_delta):
        super().update(time_delta)
        self.game.update(self.game_surface_element.image)
