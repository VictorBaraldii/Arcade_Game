import pygame
import random

pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong Arcade Game")

# Cores
white = (255,255,255)
black = (0,0,0)

# Configurações da bola
ball_size = 20
ball_speed_x = 3
ball_speed_y = 3

# Configurações da Raquestes
paddle_width = 10
paddle_height = 100
paddle_speed = 5

# Posições iniciais
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
player1_x = 10
player1_y = screen_height // 2 - paddle_width // 2
player2_x = screen_width - paddle_width - 10
player2_y = screen_height // 2 - paddle_height // 2


# Placar
score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 55)

# Exibir pontuação
def display_score():
    score_text = font.render(f"{score1} - {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

    # Movimentação da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisões parede
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Colisões raquete
    if ball_x <= player1_x + paddle_width and player1_y < ball_y < player1_y + paddle_height:
        ball_speed_x *= -1
    if ball_x >= player2_x - ball_size and player2_y < ball_y < player2_y + paddle_height:
        ball_speed_x *= -1

    # Potuação
    if ball_x < 0:
        score2 += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])
    if ball_x > screen_width:
        score1 += 1
        ball_x = screen_width // 2 - ball_size // 2
        ball_y = screen_height // 2 - ball_size // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])

    screen.fill(black)
    pygame.draw.rect(screen,white,(player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen,white,(player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen,white,(ball_x, ball_y, ball_size, ball_size))
    display_score()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()