from data.entities import *
from data.map import Map
from data.game import Game

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((900, 700))

level1_map = Map("data/level1_map.json")

# test entities
player = Knight(window.get_width() // 2, window.get_width() // 2, 30, 50, "male")

game = Game(window, clock, player, level1_map)

if __name__ == "__main__":
    while True:
        game.run()

