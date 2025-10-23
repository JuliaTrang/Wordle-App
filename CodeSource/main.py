import pygame
from wordle import loadWordList, chooseSecret, evaluateGuess, validateGuess

pygame.init()
#UI
width, height = 500, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HoangTrang's Wordle")

clock = pygame.time.Clock()
#Logic
wordLength = 5
attempts = 6
wordList = loadWordList("wordList.txt", wordLength)
secret = chooseSecret(wordList)

guess = []
results = []
currentGuess = ""
#Title appearance
padding_x = 10
padding_y = 10
font = pygame.font.SysFont("couriernew", 48)
fontTitle = pygame.font.SysFont("couriernew", 30, italic=True)
title = fontTitle.render("HoangTrang's Wordle", True, (0, 0, 0))
textRect = title.get_rect(center=(width//2, 50))
bg_rect = pygame.Rect(
    textRect.left - padding_x,
    textRect.top - padding_y,
    textRect.width + 2 * padding_x,
    textRect.height + 2 * padding_y
)
#Button UI
#Replay
buttonFont = pygame.font.SysFont("couriernew", 14, bold=True)
buttonText = buttonFont.render("Play Again", True, (255, 255, 255))
buttonRect = buttonText.get_rect(center=(330,490))
buttonBG = pygame.Rect(
    buttonRect.left - padding_x,
    buttonRect.top - padding_y,
    buttonRect.width + 2 * padding_x,
    buttonRect.height + 2 * padding_y
)
#Quit
quitText = buttonFont.render("Quit", True, (255, 255, 255))
quitRect = quitText.get_rect(center=(130, 490))
quitBG = pygame.Rect(
    quitRect.left - padding_x,
    quitRect.top - padding_y,
    quitRect.width + 2 * padding_x,
    quitRect.height + 2 * padding_y
)



colors = {"green": (83,141,78), "yellow": (181,159,59), "gray": (58,58,60)}

def drawGrid(surface):
    cellSize = 60
    startX = 95
    startY = 100
    for row in range(attempts):
        for col in range(wordLength):
            rect = pygame.Rect(startX + col * cellSize, startY + row * cellSize, cellSize, cellSize)
            pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=5)
            pygame.draw.rect(surface, (200, 200, 200), rect, width=2, border_radius=5)


def drawLetter(surface):
    cellSize = 60
    startX = 95
    startY = 100
    for r, doan in enumerate(guess):
        for c, ch in enumerate(doan):
            rect = pygame.Rect(startX + c * cellSize, startY + r * cellSize, cellSize, cellSize)
            color = colors[results[r][c]]
            pygame.draw.rect(surface, color, rect, border_radius=5)
            text = font.render(ch, True, (255, 255, 255))
            textRect = text.get_rect(center=rect.center)
            surface.blit(text, textRect)

    r = len(guess)
    for c, ch in enumerate(currentGuess):
        rect = pygame.Rect(startX + c * cellSize, startY + r * cellSize, cellSize, cellSize)
        text = font.render(ch, True, (0, 0, 0))
        textRect = text.get_rect(center=rect.center)
        surface.blit(text, textRect)


#Game loop
running = True
gameActive = True
message = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and gameActive:
            if event.key == pygame.K_RETURN:
                if len(currentGuess) == wordLength and validateGuess(currentGuess, wordList, wordLength):
                    res = evaluateGuess(currentGuess, secret)
                    guess.append(currentGuess)
                    results.append(res)
                    currentGuess = ""
                    if guess[-1] == secret:
                        message = "Congratulation! You win!"
                        gameActive = False
                    elif len(guess) >= attempts:
                        message = f"You lose! Answer is {secret}"
                        gameActive = False
                else:
                    message = "Invalid guess" 
            elif event.key == pygame.K_BACKSPACE:
                currentGuess = currentGuess[:-1]
            elif pygame.K_a <= event.key <= pygame.K_z and len(currentGuess) < wordLength:
                currentGuess += chr(event.key).upper()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if buttonBG.collidepoint(event.pos):
                    message = "Restarting game ..."
                    screen.fill((233, 235, 242))
                    drawGrid(screen)
                    drawLetter(screen)
                    text_surface = fontTitle.render(message, True, (0,0,0))
                    text_rect = text_surface.get_rect(center=(width//2, 550))
                    screen.blit(text_surface, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    message = None
                    gameActive = True
                    guess.clear()
                    results.clear()
                    currentGuess = ""
                    secret = chooseSecret(wordList)    
                elif quitBG.collidepoint(event.pos):
                    running = False 

    screen.fill((182, 187, 121))
    drawGrid(screen)
    drawLetter(screen)
    #Title draw
    titleBackgroundColor = (249, 192, 222)
    pygame.draw.rect(screen, titleBackgroundColor, textRect, border_radius=20)
    pygame.draw.rect(screen, titleBackgroundColor, bg_rect, border_radius=20)
    screen.blit(title, textRect)
    #Button draw
    #Replay
    pygame.draw.rect(screen, (153, 77, 71), buttonBG, border_radius=20)   # màu đỏ đất
    screen.blit(buttonText, buttonRect)
    #Quit
    pygame.draw.rect(screen, (153, 77, 71), quitBG, border_radius=20)   # màu đỏ đất
    screen.blit(quitText, quitRect)
    pygame.display.flip()
    clock.tick(60)

    if message:
        if message == "Congratulation! You win!":
            screen.fill((151, 161, 59))
        elif message == f"You lose! Answer is {secret}":
            screen.fill((153, 77, 71))
        elif message == "Invalid guess":
            screen.fill((243, 235, 216))
        else:
            screen.fill((233, 235, 242))
        drawGrid(screen)
        drawLetter(screen)
        text_surface = fontTitle.render(message, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(width//2, 550))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        message = None

pygame.quit()
