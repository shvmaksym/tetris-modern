import pygame
from run_game import Run

violet_screen_color = (73, 6, 72)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == GAME_UPDATE and not game_run.game_over:
            game_run.move_down()
    return True 

def handle_keys():
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

def update_screen():
    screen.fill(violet_screen_color)
    game_run.draw(screen)
    pygame.display.update()

def main():
    pygame.init()
    global GAME_UPDATE
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 250)

    global screen
    screen = pygame.display.set_mode((400, 700))
    pygame.display.set_caption("Tetris Modern")

    clock = pygame.time.Clock()

    global game_run
    game_run = Run()

    run = True
    while run:
        pygame.time.delay(50)
        run = handle_events() 
        handle_keys()
        update_screen()
        clock.tick(60)

if __name__ == "__main__":
    main()
