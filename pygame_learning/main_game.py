import pygame

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1920, 1080))

clock = pygame.time.Clock()

running = True


while running:
    # process player inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Do logical updates here

    screen.fill("white") # Fill the display with a solid color

    # RENDER the graphics here


    pygame.display.flip() # Refresh on-screen display
    clock.tick(60)        # wait until next fram at 60 FPS

pygame.quit()