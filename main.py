import pygame
from grid import Grid

violet_screen_color = (73, 6, 72)
grey = (127, 127, 127)	

def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 1000))
    pygame.display.set_caption("Tetris Modern")

    clock = pygame.time.Clock()
    
    game_grid = Grid()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(violet_screen_color)
        game_grid.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
