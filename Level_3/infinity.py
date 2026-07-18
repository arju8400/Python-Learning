import pygame
import math
import random
import sys

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("infinity")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 16)

TEXT = "FOREVER"
COLOR = (120, 200, 255)
BG_COLOR = (5, 5, 5)


def infinity_points():
    points = []
    cx, cy = W // 2, H // 2
    a = 220  # size of the lemniscate

    for i in range(300):
        t = (i / 300) * math.pi * 2
        # Lemniscate of Bernoulli parametric equations
        denom = 1 + math.sin(t) ** 2
        x = (a * math.cos(t)) / denom
        y = (a * math.sin(t) * math.cos(t)) / denom
        points.append({
            "x": cx + x,
            "y": cy + y,
            "alpha": 0,
            "target": random.uniform(150, 255),
            "delay": random.uniform(0, 5000),
        })
    return points


points = infinity_points()
start_time = pygame.time.get_ticks()


def draw_text_center():
    surf = font.render(TEXT, True, (255, 255, 255))
    rect = surf.get_rect(center=(W // 2, H // 2 + 60))
    screen.blit(surf, rect)


def main():
    global start_time
    running = True
    while running:
        elapsed = pygame.time.get_ticks() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BG_COLOR)

        for p in points:
            if elapsed >= p["delay"] and p["alpha"] < p["target"]:
                p["alpha"] = min(p["alpha"] + 2, p["target"])

            if p["alpha"] > 0:
                surf = pygame.Surface((5, 5), pygame.SRCALPHA)
                color = (*COLOR, int(p["alpha"]))
                pygame.draw.circle(surf, color, (2, 2), 2)
                screen.blit(surf, (p["x"] - 2, p["y"] - 2))

        draw_text_center()
        pygame.display.flip()
        clock.tick(60)

        if elapsed > 12000:
            for p in points:
                p["alpha"] = 0
                p["delay"] = random.uniform(0, 5000)
            start_time = pygame.time.get_ticks()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()