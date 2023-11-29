import random
import pygame


def small_heart(screen): #feature 1
    pink_1 = pygame.Color(255, 189, 213)
    pink_2 = pygame.Color(255, 140, 182)
    pink_3 = pygame.Color(255, 79, 144)
    pink_4 = pygame.Color(235, 45, 114)
    pink_5 = pygame.Color(200, 4, 75)
    white = pygame.Color(255, 255, 255)
#first pillar for N
    surf = pygame.Surface((20, 100))
    surf.fill(pink_1)
    screen.blit(surf, (300, 200))
#left most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink_2)
    screen.blit(surf, (320, 215))
#middle most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink_3)
    screen.blit(surf, (340, 238))
#right most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink_4)
    screen.blit(surf, (355, 260))
#second pillar for N/ pillar for F
    surf = pygame.Surface((20, 100))
    surf.fill(pink_5)
    screen.blit(surf, (375, 200))
#top stroke of F
    surf = pygame.Surface((90, 20))
    surf.fill(white)
    screen.blit(surf, (375, 200))
#middle stroke of F
    surf = pygame.Surface((50, 20))
    surf.fill(white)
    screen.blit(surf, (375, 238))


def big_heart(screen): #feature 2
    rainbow = pygame.Color(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#left eye
    surf2 = pygame.Surface((15,15))
    surf2.fill(rainbow)
    screen.blit(surf2, (445, 300))
#right eye
    surf2 = pygame.Surface((15,15))
    surf2.fill(rainbow)
    screen.blit(surf2, (515, 300))
#middle part of mouth
    surf2 = pygame.Surface((115,15))
    surf2.fill(rainbow)
    screen.blit(surf2, (430, 350))
#left mouth curve
    surf2 = pygame.Surface((15,30))
    surf2.fill(rainbow)
    screen.blit(surf2, (415, 325))
#right mouth curve
    surf2 = pygame.Surface((15,30))
    surf2.fill(rainbow)
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
