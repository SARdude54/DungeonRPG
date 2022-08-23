import pygame


def load_image(path: str, size: list | tuple, colorkey: list | tuple, flip_x: bool = False, flip_y: bool = False):
    if flip_x or flip_y:
        image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(path), size), flip_x, flip_y)
        image.set_colorkey(colorkey)
        return image
    image = pygame.transform.scale(pygame.image.load(path), size)
    image.set_colorkey(colorkey)
    return image


def load_animation(folder: str, file: str, frames: int, size: list | tuple, colorkey: list | tuple,
                   flip_x: bool = False, flip_y: bool = False):
    num_index = file.find("1")
    if flip_x or flip_y:
        frames = [
            pygame.transform.flip(
                pygame.transform.scale(pygame.image.load(f"{folder}//{file[:num_index]}{i}.png"), size), flip_x, flip_y)
            for i in range(0, frames)]
        for frame in frames:
            frame.set_colorkey(colorkey)
        return frames

    frames = [
        pygame.transform.scale(pygame.image.load(f"{folder}//{file[:num_index]}{i}.png"), size)
        for i in range(0, frames)]
    for frame in frames:
        frame.set_colorkey(colorkey)
    return frames
