import random
import pygame


class Particle():

    def __init__(self, pos=(0,0), size=15, life=1000):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(
            random.randint(200, 255), random.randint(0, 200), random.randint(0, 200))
        self.age = 0 # in milliseconds
        self.life = life # in milliseconds
        self.dead = False
        self.alpha = 255
        self.surface =self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))

    def update_surface(self):
        surf = pygame.Surface((self.size*0.8, self.size*0.8))
        pygame.draw.ellipse(surf, self.color, surf.get_rect())
        return surf
    
    def draw(self, surface):
        if self.dead:
            return
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)


class ParticleTrail():

    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles= []

    def update(self, dt):
        particle = Particle(self.pos, size=self.size, life=self.life)
        self.particles.insert(0, particle)
        self._update_particles(dt)
        self._update_pos()

    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Rain():

    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.particle_size = 15
        self.birth_rate = 1 # trails per frame
        self.trails = []

    def update(self, dt):
        self._birth_new_trails()
        self._update_trails(dt)

    def _update_trails(self, dt):
        for idx, trail in enumerate(self.trails):
            trail.update(dt)
            if self._trail_is_offscreen(trail):
                del self.trails[idx]

    def _trail_is_offscreen(self, trail):
        tail_is_offscreen = trail.particles[-1].pos[1] > self.screen_res[1]
        return tail_is_offscreen

    def _birth_new_trails(self):
        for count in range(self.birth_rate):
            screen_width = self.screen_res[0]
            x = random.randrange(0, screen_width, self.particle_size)
            pos = (x, 0)
            life = random.randrange(500, 3000)
            trail = ParticleTrail(pos, self.particle_size, life)
            self.trails.insert(0, trail)

    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)


def main():
    pygame.init()
    pygame.display.set_caption("Heart Beat with Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    rain = Rain(resolution)
    running = True
    show_symbol = True
    show_face = False
    full_screen = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    background = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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

        rain.update(dt)

        if show_symbol:
            small_heart(screen)
        if show_face:
            big_heart(screen)

        rain.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


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


if __name__ == "__main__":
    main()
