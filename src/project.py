import pygame


def small_heart(screen): #feature 1
    pink_1 = pygame.Color(255, 186, 211)
    pink_2 = pygame.Color(255, 105, 160)
    pink_3 = pygame.Color(255, 38, 118)
    pink_4 = pygame.Color(222, 0, 81)
    pink_5 = pygame.Color(145, 0, 53)
    white = pygame.Color(255, 255, 255)
#pink_1 upper square
    surf = pygame.Surface((40, 40))
    surf.fill(pink_1)
    screen.blit(surf, (300, 200))
#pink_1 lower square
    surf = pygame.Surface((40, 40))
    surf.fill(pink_1)
    screen.blit(surf, (280, 220))
#pink_2 right square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_2)
    screen.blit(surf, (360, 200))
#pink_2 middle rectangle
    surf = pygame.Surface((20, 40))
    surf.fill(pink_2)
    screen.blit(surf, (340, 220))
#pink_2 left rectangle
    surf = pygame.Surface((20, 40))
    surf.fill(pink_2)
    screen.blit(surf, (320, 240))
#pink_2 left square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_2)
    screen.blit(surf, (300, 260))
#pink_3 top right square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_3)
    screen.blit(surf, (380, 200))
#pink_3 right rectangle
    surf = pygame.Surface((20, 40))
    surf.fill(pink_3)
    screen.blit(surf, (360, 220))
#pink_3 middle square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_3)
    screen.blit(surf, (340, 260))
#pink_3 left square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_3)
    screen.blit(surf, (320, 280))
#pink_4 right rectangle
    surf = pygame.Surface((20, 40))
    surf.fill(pink_4)
    screen.blit(surf, (380, 220))
#pink_4 middle square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_4)
    screen.blit(surf, (360, 260))
#pink_4 left square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_4)
    screen.blit(surf, (340, 280))
#pink_5 right rectangle
    surf = pygame.Surface((20, 40))
    surf.fill(pink_5)
    screen.blit(surf, (400, 220))
#pink_5 right square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_5)
    screen.blit(surf, (380, 260))
#pink_5 middle square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_5)
    screen.blit(surf, (360, 280))
#pink_5 left square
    surf = pygame.Surface((20, 20))
    surf.fill(pink_5)
    screen.blit(surf, (340, 300))


def big_heart(screen): #feature 2
    pink_1 = pygame.Color(255, 186, 211)
    pink_2 = pygame.Color(255, 105, 160)
    pink_3 = pygame.Color(255, 38, 118)
    pink_4 = pygame.Color(222, 0, 81)
    pink_5 = pygame.Color(145, 0, 53)
    white = pygame.Color(255, 255, 255)
#left eye
    surf2 = pygame.Surface((15,15))
    surf2.fill(pink_1)
    screen.blit(surf2, (445, 300))
#right eye
    surf2 = pygame.Surface((15,15))
    surf2.fill(pink_2)
    screen.blit(surf2, (515, 300))
#middle part of mouth
    surf2 = pygame.Surface((115,15))
    surf2.fill(pink_3)
    screen.blit(surf2, (430, 350))
#left mouth curve
    surf2 = pygame.Surface((15,30))
    surf2.fill(pink_4)
    screen.blit(surf2, (415, 325))
#right mouth curve
    surf2 = pygame.Surface((15,30))
    surf2.fill(pink_5)
    screen.blit(surf2, (545, 325))


def main():
    pygame.init()
    pygame.display.set_caption("Heart Beat")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    show_symbol = True
    show_face = False
    full_screen = False
    while running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_symbol = not show_symbol
                    show_face = not show_face
                elif event.type == pygame.KEYDOWN:
                    event.key == pygame.K_f
                    full_screen = not full_screen
                    if full_screen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode(resolution)
        # game logic
        # render & display phase
        black = pygame.Color(0, 0, 0)
        screen.fill(black)

        if show_symbol:
            small_heart(screen)
        if show_face:
            big_heart(screen)

        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()
