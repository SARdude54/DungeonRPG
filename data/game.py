import sys

from .entities import *
from .map import Map


class Game:
    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, player: Hero, map: Map):
        self.screen = screen
        self.clock = clock
        self.player = player
        self.map = map
        self.chort = Chort(500, 300, 50, 50)
        self.big_demon = BigDemon(150, 300, 75, 100)
        self.rendered_entities = [self.chort, self.big_demon]

    def init_loop(self):
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(str(self.clock.get_fps()))
        self.clock.tick(60)

        self.map.check_tile_collisions(self.player)
        self.player.check_collisions()

    def render(self):
        self.map.render(self.screen)
        self.chort.render(self.screen)
        self.big_demon.render(self.screen)
        self.player.render(self.screen)

    def _move_up(self):
        self.map.translate_down()
        for entity in self.rendered_entities:
            entity.rect.y += 5

    def _move_down(self):
        self.map.translate_up()
        for entity in self.rendered_entities:
            entity.rect.y += -5

    def _move_right(self):
        self.map.translate_left()
        for entity in self.rendered_entities:
            entity.rect.x += -5

    def _move_left(self):
        self.map.translate_right()
        for entity in self.rendered_entities:
            entity.rect.x += 5

    def update(self):

        if self.player.is_moving_up():
            self._move_up()

        if self.player.is_moving_down():
            self._move_down()

        if self.player.is_moving_left():
            self._move_left()

        if self.player.is_moving_right():
            self._move_right()

    def run(self):
        while True:
            self.init_loop()

            self.run_events()

            self.update()

            self.render()

            pygame.display.update()

    def run_events(self):
        keys = pygame.key.get_pressed()

        # Check movements
        if keys[K_d] and not keys[K_a]:
            self.player.set_moving_right()
            self.map.set_moving_left()

        elif keys[K_a] and not keys[K_d]:
            self.player.set_moving_left()
            self.map.set_moving_right()

        else:
            self.player.set_horizontal_idle()
            self.map.set_horizontal_idle()

        if keys[K_w] and not keys[K_s]:
            self.player.set_moving_up()
            self.map.set_moving_down()

        elif keys[K_s] and not keys[K_w]:
            self.player.set_moving_down()
            self.map.set_moving_up()

        else:
            self.player.set_vertical_idle()
            self.map.set_vertical_idle()

        # events
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
