import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((300, 600))
    pygame.display.set_caption("Tetris modern")

    clock = pygame.time.Clock()

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
