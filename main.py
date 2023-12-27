import pygame
import sys
from run_game import Run
from colors import Colors


def start_screen():
    screen.fill(Colors.black)

    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    hint_rect = hint_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    screen.blit(title_text, title_rect.topleft)
    screen.blit(hint_text, hint_rect.topleft)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
            
def paused_screen():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause = False

        pygame.draw.rect(screen, Colors.black, paused_rect)
        screen.blit(paused_text, paused_rect)
        pygame.display.update()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            paused_screen()
        if event.type == GAME_UPDATE:
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
        pygame.time.delay(100)
        game_run.current.rotate()

def update_screen():
    screen.fill(Colors.screen_color)
    game_run.draw(screen)

    screen.blit(score_surface, (30, 610, 5, 5))
    screen.blit(next_block_surface, (185, 610, 5, 5))

    pygame.draw.rect(screen, Colors.black, score_rect)
    pygame.draw.rect(screen, Colors.black, next_block_rect)
    pygame.display.update()

def main():
    pygame.init()

    global GAME_UPDATE
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, 500)

    global screen
    screen = pygame.display.set_mode((300, 800))
    pygame.display.set_caption("Tetris Modern")

    global score_surface, next_block_surface, game_over_surface
    title_font = pygame.font.SysFont('arial', 34, bold=True)
    hint_font = pygame.font.SysFont('arial', 30, bold=True)
    score_surface = title_font.render("Score", True, Colors.white)
    next_block_surface = title_font.render("Next", True, Colors.white)
    game_over_surface = title_font.render("Game Over", True, Colors.white)
    
    global score_rect, next_block_rect
    score_rect = pygame.Rect(20, 650, 110, 70)
    next_block_rect = pygame.Rect(170, 650, 110, 70)

    global pause, paused_text, paused_rect
    pause = False
    paused_font = pygame.font.SysFont('arial', 50, bold=True)
    paused_text = paused_font.render("Paused", True, Colors.white)
    paused_rect = pygame.Rect(60, 280, 180, 60)

    global title_text, hint_text
    title_text = title_font.render("Tetris Modern", True, Colors.pink)
    hint_text = hint_font.render("Press Enter to start", True, Colors.pink)

    clock = pygame.time.Clock()

    global game_run
    game_run = Run()

    start_screen()
    run = True
    while run:
        if run:
            run = handle_events() 
            handle_keys()
            update_screen()
            clock.tick(30)

if __name__ == "__main__":
    main()
