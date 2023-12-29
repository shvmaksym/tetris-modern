import pygame
import sys
from run_game import Run
from colors import Colors


def start_screen():
    screen.fill(Colors.black)

    title_rect = title_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 50)
    )
    hint_rect = hint_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )

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


def game_over():
    screen.fill(Colors.black)

    game_over_rect = game_over_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 50)
    )
    reset_hint_rect = reset_hint_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )
    your_score_rect = your_score_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 100)
    )
    score_value_rect = score_value_text.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 150)
    )

    screen.blit(game_over_text, game_over_rect.topleft)
    screen.blit(reset_hint_text, reset_hint_rect.topleft)
    screen.blit(your_score_text, your_score_rect.topleft)
    screen.blit(score_value_text, score_value_rect.topleft)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_run.reset()
                pygame.time.set_timer(GAME_UPDATE, game_run.speed)
                game_run.game_over = False
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
                return

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
            update_speed()

    return True


def handle_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        game_run.move_left()

    if keys[pygame.K_RIGHT]:
        game_run.move_right()

    if keys[pygame.K_DOWN]:
        game_run.move_down()
        game_run.change_score(1, 0)

    if keys[pygame.K_SPACE]:
        pygame.time.delay(100)
        game_run.change_position()


def update_score_and_next_block_and_level():
    global score_value_text, level_value
    level_value = title_font.render(str(game_run.level), True, Colors.white)
    score_value_text = title_font.render(str(game_run.score), True, Colors.white)
    score_value_rect = score_value_text.get_rect()

    x = score_rect.centerx - score_value_rect.width // 2
    y = score_rect.centery - score_value_rect.height // 2

    screen.blit(score_value_text, (x, y))
    screen.blit(level_value, (100, 740))
    game_run.next.draw(screen, 160, 660)


def update_screen():  
    screen.fill(Colors.screen_color) 
    game_run.draw(screen)
    
    screen.blit(score_text, (30, 610, 5, 5))
    screen.blit(next_block_text, (175, 610, 5, 5))
    screen.blit(level_text, (30, 740, 5, 5))

    pygame.draw.rect(screen, Colors.black, score_rect)
    pygame.draw.rect(screen, Colors.black, next_block_rect)

    update_score_and_next_block_and_level()

    pygame.display.update()


def update_speed():
    game_run.change_speed()
    if game_run.speed_changed:
        pygame.time.set_timer(GAME_UPDATE, game_run.speed)
        game_run.speed_changed = False


def __init__():
    global title_font

    title_font = pygame.font.SysFont("arial", 34, bold=True)
    hint_font = pygame.font.SysFont("arial", 25)
    paused_font = pygame.font.SysFont("arial", 50, bold=True)

    global score_text, next_block_text, game_over_text, paused_text, title_text, hint_text, reset_hint_text, your_score_text, score_value_text, level_text

    score_text = title_font.render("Score", True, Colors.white)
    next_block_text = title_font.render("Next", True, Colors.white)
    level_text = title_font.render("Lvl. ", True, Colors.white)
    paused_text = paused_font.render("Paused", True, Colors.white)
    game_over_text = title_font.render("Game Over", True, Colors.white)
    your_score_text = title_font.render("Your score :", True, Colors.white)
    title_text = title_font.render("Tetris Modern", True, Colors.pink)
    hint_text = hint_font.render("Press Enter to start", True, Colors.pink)
    reset_hint_text = hint_font.render("Press Enter to restart", True, Colors.pink)

    global score_rect, next_block_rect, paused_rect

    score_rect = pygame.Rect(20, 650, 110, 70)
    next_block_rect = pygame.Rect(150, 650, 130, 110)
    paused_rect = pygame.Rect(60, 280, 180, 60)


def main():
    pygame.init()

    global game_run
    game_run = Run()

    global GAME_UPDATE
    GAME_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(GAME_UPDATE, game_run.speed)

    global screen
    screen = pygame.display.set_mode((300, 800))
    pygame.display.set_caption("Tetris Modern")
    
    global pause
    pause = False

    clock = pygame.time.Clock()

    __init__()
    start_screen()

    run = True
    while run:
        if game_run.game_over: 
            game_over()
        if run:
            run = handle_events()
            handle_keys()
            update_screen()
            clock.tick(30)


if __name__ == "__main__":
    main()
