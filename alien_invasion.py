import sys

import pygame

# importing settings class

from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # set dimensions of window and caption - now coded according to settings class

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Set background color.
        self.bg_color = self.settings.bg_color
        # RGB colors - (230, 230, 230) gives an equal mix of red, green, and blue
        # now coded according to settings class

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # Code to quit the game
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop with the background color.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
