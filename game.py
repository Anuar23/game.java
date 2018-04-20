import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
points = [100, 100]
width = 40
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: points[1] -= 2
        if pressed[pygame.K_DOWN]: points[1] += 2
        if pressed[pygame.K_LEFT]: points[0] -= 2
        if pressed[pygame.K_RIGHT]: points[0] += 2
        if pressed[pygame.K_2]: width -=2
        if pressed[pygame.K_1]: width +=2
        
        screen.fill((0, 0, 0))
        if is_blue: color = (255, 255, 255)
        else: color = (128, 128, 128)

        pygame.draw.circle(screen, color, points, width)
        pygame.display.flip()
        clock.tick(60)
