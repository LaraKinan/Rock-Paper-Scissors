import random
import pygame

ROCK = 1
PAPER = 2
SCISSORS = 3
screen_width, screen_height= 600, 400
background_color = (200, 173, 127)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.text = text
        self.callback = callback

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

def choose_winner(turn1, turn2):
    win1, win2, tie = 1, 2, 0
    if turn1 == turn2:
        text = font.render("It's a tie.", True, BLACK)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        return tie
    if (turn1 == ROCK and turn2 == SCISSORS) or (turn1 == PAPER and turn2 == ROCK) or (turn1 == SCISSORS and turn2 == PAPER):
        text = font.render("You win!!!", True, BLACK)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        return win1
    text = font.render("You lose!", True, BLACK)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    return win2

def get_image(turn):
    if turn == ROCK:
        return rock_image
    if turn == PAPER:
        return paper_image
    if turn == SCISSORS:
        return scissors_image
    
def choose(turn):
    global turn1, turn2
    if turn == ROCK:
        turn1 = ROCK
    elif turn == PAPER:
        turn1 = PAPER
    else:
        turn1 = SCISSORS
    turn2 = random.randint(1, 3)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.Font(None, 36)
running = True

# import images
rock_image = pygame.image.load("rock.png")
paper_image = pygame.image.load("paper.png")
scissors_image = pygame.image.load("scissors.png")

# Choice buttons
rock_button = Button(60, screen_height - 40, 140, 30, "Rock", lambda: choose(ROCK))
paper_button = Button(230, screen_height - 40, 140, 30, "Paper", lambda: choose(PAPER))
scissors_button = Button(400, screen_height - 40, 140, 30, "Scissors", lambda: choose(SCISSORS))

turn1, turn2 = 0, 0


while running:
    # Changing surface color
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rock_button.handle_event(event)
                paper_button.handle_event(event)
                scissors_button.handle_event(event)
                if turn1 == 0:
                    continue
    if not (turn1 == 0 or turn2 == 0):
        cell_rect = pygame.Rect(50, 100, 150, 150)
        screen.blit(get_image(turn1), cell_rect)
        cell_rect = pygame.Rect(screen_width - 200, 100, 150, 150)
        screen.blit(pygame.transform.flip(get_image(turn2), True, False), cell_rect)
        choose_winner(turn1, turn2)

    rock_button.draw()
    paper_button.draw()
    scissors_button.draw()
    pygame.display.flip()

pygame.quit()