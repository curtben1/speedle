import pygame

# draw a blank window
def drawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()

# main function
def main():
    run = True
    drawWindow()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Create a text box that says "hi"
                    font = pygame.font.Font(None, 36)
                    text = font.render("hi", True, (128, 128, 128))
                    text_rect = text.get_rect(center=(640, 360))
                    win.blit(text, text_rect)
                    pygame.display.update()


    pygame.quit()

# initialize the game
pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("First Game")
main()