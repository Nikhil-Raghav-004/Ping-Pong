import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

exit_button = pygame.Rect(600,550,200,50)
play_button = pygame.Rect(0,0,200,50)

screen = pygame.display.set_mode((screen_width,screen_height))

Tamil_Nadu = True

font = pygame.font.SysFont("papyrus",35)
exit_text = font.render("Exit",True,"Black")
play_text =  font.render("Play",True,"Black")

# bg_color = pygame.Color((255,243,0))
Ping_PongBG = pygame.image.load("Ping_Pong_Background.jpg")
Ping_PongBG = pygame.transform.scale(Ping_PongBG,(800,600))

bg_color = pygame.Color(('black'))
def bounc_ball():
    Tamil_Nadu = True
    rectx, recty = 140, 585

    speed = 2
    # bg_color = pygame.Color((255,243,0))
    bg_color = pygame.Color(('black'))
    clock = pygame.time.Clock()

    circx, circy = 10, 10
    speedx, speedy = 2, 1.5

    circX, circY = 350, 20
    speedX, speedY = 1, 1

    CIRCX, CIRCY = 750, 35
    SPEEDX, SPEEDY = 5, 4.5

    font = pygame.font.Font(None, 30)

    score = 0

    while Tamil_Nadu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Tamil_Nadu = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d]) and paddle.right <= screen_width:
            rectx += speed
        if (keys[pygame.K_a]) and paddle.left >= 0:
            rectx -= speed

        circx += speedx
        circy += speedy

        if circx + 10 > screen_width or circx - 10 < 0:
            speedx = -speedx

        if circy - 10 < 0:
            speedy = -speedy

        if circy + 10 > screen_height:
            circx = random.choice([500, 10])
            circy = 10

        CIRCX -= SPEEDX
        CIRCY += SPEEDY

        if circX + 10 > screen_width or circX - 10 < 0:
            speedX = -speedX

        if circY - 10 < 0:
            speedY = -speedY

        if circY + 10 > screen_height:
            circX = random.choice([250, 10])
            circY = 10

        circX += speedX
        circY += speedY

        paddle = pygame.Rect(rectx, recty, 80, 10)
        ball = pygame.Rect(circx, circy, 17, 17)
        ball2 = pygame.Rect(CIRCX, CIRCY, 8, 8)
        score_reducer = pygame.Rect(circX, circY, 30, 30)

        if ball.colliderect(paddle):
            speedy = -speedy
            score = score + 1
        if ball2.colliderect(paddle):
            SPEEDY = -SPEEDY
            score = score + 5
        if score_reducer.colliderect(paddle):
            speedY = -speedY
            score = score - 5

        if score % 10 == 0 and score != 0:
            CIRCX, CIRCY = 750, 35
            CIRCX -= SPEEDX
            CIRCY += SPEEDY

        if score % 5 == 0 and score != 0:
            circX, circY = 750, 35
            circX -= speedX
            circY += speedY

        if score > 100 or score < 0:
            Tamil_Nadu = False

        # screen.fill(bg_color)
        screen.blit(Ping_PongBG,(0,0))

        pygame.draw.rect(screen, 'white', paddle)
        pygame.draw.circle(screen, 'Green', (circx, circy), 17)
        pygame.draw.circle(screen, 'red', (CIRCX, CIRCY), 5)
        pygame.draw.circle(screen, 'Blue', (CIRCX, CIRCY), 8, 2)
        pygame.draw.circle(screen, 'White', (circX, circY), 30)

        text = font.render(f" Score:{score}", True, 'red')
        screen.blit(text, (screen_width - 100, 10))

        clock.tick(500)

        pygame.display.update()

    return



while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False

        if  event.type == pygame.MOUSEBUTTONDOWN and exit_button.collidepoint(event.pos):
            Tamil_Nadu = False

        if event.type ==pygame.MOUSEBUTTONDOWN and play_button.collidepoint(event.pos):
            bounc_ball()


    screen.fill(bg_color)

    pygame.draw.rect(screen, "red", exit_button,border_radius = 10)

    pygame.draw.rect(screen, "green", play_button,border_radius = 10)

    font = pygame.font.SysFont("papyrus", 100)
    text1 = font.render("Ping Pong",True,'Blue')


    screen.blit(exit_text, (exit_button.x + 70, exit_button.y))
    screen.blit(play_text, (play_button.x + 70, play_button.y))
    screen.blit(text1,(210,210))



    pygame.display.flip()