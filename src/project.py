import random
import pygame


def nf_symbol(screen): #feature 1
    pink = pygame.Color(255, 193, 204)
#first pillar for N
    surf = pygame.Surface((20, 100))
    surf.fill(pink)
    screen.blit(surf, (300, 200))
#left most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink)
    screen.blit(surf, (320, 215))
#middle most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink)
    screen.blit(surf, (340, 238))
#right most middle slash for N
    surf = pygame.Surface((20, 25))
    surf.fill(pink)
    screen.blit(surf, (355, 260))
#second pillar for N/ pillar for F
    surf = pygame.Surface((20, 100))
    surf.fill(pink)
    screen.blit(surf, (375, 200))
#top stroke of F
    surf = pygame.Surface((90, 20))
    surf.fill(pink)
    screen.blit(surf, (375, 200))
#middle stroke of F
    surf = pygame.Surface((50, 20))
    surf.fill(pink)
    screen.blit(surf, (375, 238))


def smiley_face(screen): #feature 2
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
    pygame.display.set_caption("Digital Rain")
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
        rain.update(dt)
        # render & display phase
        black = pygame.Color(0, 0, 0)
        screen.fill(black)

        if show_symbol:
            nf_symbol(screen)
        if show_face:
            smiley_face(screen)

        rain.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


if __name__ == "__main__":
    main()