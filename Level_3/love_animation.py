import pygame
import math
import random
import sys

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("broken_heart")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 13)

TEXT = "LOVE YOU"
HEART_COLOR = (255, 77, 109)
BG_COLOR = (5, 5, 5)


def heart_points():
    points = []
    cx, cy = W // 2, H // 2
    scale = min(W, H) / 45

    # Outer ring
    for i in range(180):
        t = (i / 180) * math.pi * 2
        x = 16 * math.pow(math.sin(t), 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        points.append({
            "x": cx + x * scale,
            "y": cy + y * scale,
            "alpha": 0,
            "target": random.uniform(180, 255),
            "delay": random.uniform(0, 6000),
        })

    # Inner rings (filled scatter of the heart shape)
    for s in [0.2, 0.4, 0.6, 0.8]:
        for i in range(80):
            t = (i / 80) * math.pi * 2
            x = 16 * math.pow(math.sin(t), 3)
            y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
            jitter_x = random.uniform(-0.5, 0.5)
            jitter_y = random.uniform(-0.5, 0.5)
            points.append({
                "x": cx + (x + jitter_x) * scale * s,
                "y": cy + (y + jitter_y) * scale * s,
                "alpha": 0,
                "target": random.uniform(80, 180),
                "delay": random.uniform(0, 8000),
            })

    return points


points = heart_points()
start_time = pygame.time.get_ticks()


def draw_text_center():
    text_surface = font.render(TEXT, True, (255, 255, 255))
    rect = text_surface.get_rect(center=(W // 2, H // 2))
    screen.blit(text_surface, rect)


def main():
    running = True
    while running:
        now = pygame.time.get_ticks()
        elapsed = now - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BG_COLOR)

        for p in points:
            if elapsed >= p["delay"]:
                if p["alpha"] < p["target"]:
                    p["alpha"] = min(p["alpha"] + 2, p["target"])

            if p["alpha"] > 0:
                surf = pygame.Surface((4, 4), pygame.SRCALPHA)
                color = (*HEART_COLOR, int(p["alpha"]))
                pygame.draw.circle(surf, color, (2, 2), 2)
                screen.blit(surf, (p["x"] - 2, p["y"] - 2))

        draw_text_center()

        pygame.display.flip()
        clock.tick(60)

        # Restart animation loop after everything has faded in + a pause
        if elapsed > 16000:
            for p in points:
                p["alpha"] = 0
                p["delay"] = random.uniform(0, 6000) if p in points[:180] else random.uniform(0, 8000)
            nonlocal_reset()

    pygame.quit()
    sys.exit()


def nonlocal_reset():
    global start_time
    start_time = pygame.time.get_ticks()


if __name__ == "__main__":
    main()