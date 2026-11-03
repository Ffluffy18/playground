import sys, pygame
pygame.init()

size = width, height = 1920, 1080
speed = [1, 1]
black = 0, 0, 0
balo_size = (132, 132)

screen = pygame.display.set_mode(size) # creates a Surface object that is the actual displayed graphis, and where you will draw stuff

balo = pygame.image.load("BALO fantasy-pack all.gif").convert_alpha()# returns a Surface will the image
balo = pygame.transform.scale(balo, balo_size)
balorect = balo.get_rect() # rectangular area which can be used to manage position of an object in the screen







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


        # Balo movement ??????
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("KEY PRESSED")
                balorect.top += 10


    screen.fill(black)
    screen.blit(balo, balorect) # Surface.blit() method handles image drawing, blit means copying pixel colors from one image to another
    pygame.display.flip()

    