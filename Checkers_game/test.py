import pygame
# Set up some constants
WIDTH = 500
HEIGHT = 500
# Initialize Pygame
pygame.init()
# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
# Set up the clock
clock = pygame.time.Clock()
# Set up the circle properties
x = 0
y = HEIGHT/2
radius = 50
color = (0,0,255)
# Game loop
running = True
while running:
    # keep the loop running at the right speed
    clock.tick(60)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    x += 1
    if x > WIDTH:
        x = 0 - radius
    # Draw
    win.fill((255,255,255))
    pygame.draw.circle(win, color, (x, y), radius)
    pygame.draw.circle(win, color, (x+20, y), 25 + 2)
    pygame.draw.circle(win, color, (x+50, y), 25)

    # After drawing everything, flip the display
    pygame.display.flip()
pygame.quit()