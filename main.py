import pygame

violet_screen_color = (73, 6, 72)

def main():
    pygame.init()

    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Tetris Modern")

    clock = pygame.time.Clock()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(violet_screen_color)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
