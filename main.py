import pygame
from run_game import Run

violet_screen_color = (73, 6, 72)

game_run = Run()



def main():
    pygame.init()

    screen = pygame.display.set_mode((500, 1000))
    pygame.display.set_caption("Tetris Modern")

    clock = pygame.time.Clock()
    
    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            game_run.move_left()

        if keys[pygame.K_RIGHT]:
            game_run.move_right()
            
        if keys[pygame.K_DOWN]:
            game_run.move_down()
        
        if keys[pygame.K_SPACE]:
            pygame.time.delay(50)
            game_run.current.rotate()


        screen.fill(violet_screen_color)
        game_run.draw(screen)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
