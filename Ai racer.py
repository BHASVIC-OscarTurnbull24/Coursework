import pygame

pygame.init() #Initialises pygame so its functionality can be used

screen = pygame.display.set_mode((800, 600)) #Creates a display window with 800 horizontal pixels and 600 vertical pixels


running = True
while running: #Infinite loop to prevent the display window from closing until the user decides to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()


