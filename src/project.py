import pygame
import random

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
#white square
    surf = pygame.Surface((20, 20))
    surf.fill(white)
    screen.blit(surf, (300, 220))


def big_heart(screen): #feature 2
    pink_1 = pygame.Color(255, 186, 211)
    pink_2 = pygame.Color(255, 105, 160)
    pink_3 = pygame.Color(255, 38, 118)
    pink_4 = pygame.Color(222, 0, 81)
    pink_5 = pygame.Color(145, 0, 53)
    white = pygame.Color(255, 255, 255)
#pink_1 giant rectangle
    surf2 = pygame.Surface((60,80))
    surf2.fill(pink_1)
    screen.blit(surf2, (280, 180))
#pink_1 left rectangle
    surf2 = pygame.Surface((20, 60))
    surf2.fill(pink_1)
    screen.blit(surf2, (260, 200))
#pink_1 right rectangle
    surf2 = pygame.Surface((20, 40))
    surf2.fill(pink_1)
    screen.blit(surf2, (340, 200))
#pink_1 bottom rectangle
    surf2 = pygame.Surface((40, 20))
    surf2.fill(pink_1)
    screen.blit(surf2, (280, 260))
#pink_1 top square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_1)
    screen.blit(surf2, (360, 180))
#pink_2 top square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_2)
    screen.blit(surf2, (380, 180))
#pink_2 right rectangle
    surf2 = pygame.Surface((20, 60))
    surf2.fill(pink_2)
    screen.blit(surf2, (360, 200))
#pink_2 middle rectangle
    surf2 = pygame.Surface((20, 40))
    surf2.fill(pink_2)
    screen.blit(surf2, (340, 240))
#pink_2 left rectangle
    surf2 = pygame.Surface((20, 40))
    surf2.fill(pink_2)
    screen.blit(surf2, (320, 260))
#pink_2 left square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_2)
    screen.blit(surf2, (300, 280))
#pink_3 top square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_3)
    screen.blit(surf2, (400, 180))
#pink_3 right rectangle
    surf2 = pygame.Surface((20, 60))
    surf2.fill(pink_3)
    screen.blit(surf2, (380, 200))
#pink_3 right square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_3)
    screen.blit(surf2, (360, 260))
#pink_3 middle square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_3)
    screen.blit(surf2, (340, 280))
#pink_3 left square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_3)
    screen.blit(surf2, (320, 300))
#pink_4 right rectangle
    surf2 = pygame.Surface((20, 60))
    surf2.fill(pink_4)
    screen.blit(surf2, (400, 200))
#pink_4 right square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_4)
    screen.blit(surf2, (380, 260))
#pink_4 middle square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_4)
    screen.blit(surf2, (360, 280))
#pink_4 left square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_4)
    screen.blit(surf2, (340, 300))
#pink_5 right rectangle
    surf2 = pygame.Surface((20, 60))
    surf2.fill(pink_5)
    screen.blit(surf2, (420, 200))
#pink_5 top right square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_5)
    screen.blit(surf2, (400, 260))
#pink_5 middle right square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_5)
    screen.blit(surf2, (380, 280))
#pink_5 middle left square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_5)
    screen.blit(surf2, (360, 300))
#pink_5 bottom square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(pink_5)
    screen.blit(surf2, (340, 320))
#top white square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(white)
    screen.blit(surf2, (300, 200))
#bottom white square
    surf2 = pygame.Surface((20, 20))
    surf2.fill(white)
    screen.blit(surf2, (280, 220))


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
                    background = pygame.Color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                    screen.fill(background)
                    show_symbol = not show_symbol
                    show_face = not show_face
                elif event.type == pygame.KEYDOWN:
                    event.key == pygame.K_f
                    full_screen = not full_screen
                    if full_screen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode(resolution)


        if show_symbol:
            small_heart(screen)
        if show_face:
            big_heart(screen)

        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()
    