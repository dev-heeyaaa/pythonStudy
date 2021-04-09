import pygame
import sys
import random

def showScore(score, x, y, screen):
    font = pygame.font.Font(None, 24) # 출력할 글씨의 폰트 스타일과 크기 지정
    text = font.render("Score: "+str(score).zfill(6), True, (0, 0, 0)) # 출력할 글씨를 생성하는 코드/ anti얼라이씽? 적용을 하겠다(True): 계단현상을 막겠다
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    screen.blit(text, textRect)


pygame.init()
screen = pygame.display.set_mode((480, 640))

FPS = 30
fpsClock = pygame.time.Clock()

# 타이머는 주기적으로 위에서 아래로 떨어질 행성의 타이밍
asteroidtimer = 100

# 첫 번째로 떨어지는 행성의 정보
asteroids = [[20, 0, 0]]

# 기본 점수 0점 초기화
score = 0

try:
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)

    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")

    takeoffsound.play()

except Exception as err:
    print("그림 또는 효과음 삽입에 문제가 있습니다.", err)
    pygame.quit()
    sys.exit(0)

running = True
while running:
    fpsClock.tick(FPS)

    screen.fill((255, 255, 255))

    score = score + 1 # 1 초에 30번?
    showScore(score, 400, 10, screen) # (현재 출력할 점수를, x, y, 어떤 스크린에 표시되어야할지)
    if score % 100 == 0:
        FPS += 2
        # 연산의 속도 증가. 난이도 올라가는 효과

    # 화면 상의 현재 마우스 위치
    position = pygame.mouse.get_pos()
    spaceshippos = (position[0]-10, 600)
    screen.blit(spaceshipimg, spaceshippos)

    spaceshipRect = pygame.Rect(spaceshipimg.get_rect())
    spaceshipRect.left = spaceshippos[0]
    spaceshipRect.top = spaceshippos[1]

    # 떨어질 행성을 생성하고
    asteroidtimer -= 10 # y축 10만큼 증가 / 천천히 부드럽게 떨어지고 싶으면 숫자를 줄이자.
    if asteroidtimer <= 0:
        randomX = random.randint(5, 475)
        asteroidType = random.randint(0, 2) # 행성 0, 1, 2 중 핸덤으로 떨어진다
        asteroids.append([randomX, 0, asteroidType]) # y좌표가 0
        asteroidtimer = random.randint(50, 200) # 타이머 초기화 행성 랜덤욿 떨어트리기

    # 생성한 행성을 떨어뜨린다
    index = 0
    for stone in asteroids:
        stone[1] += 10 # 떨어질, 떨어지고 있는 행서의 정보를 하나씩 꺼내서 n번째 행성에 y좌표를

        if stone[1] > 640:
            asteroids.pop(index)

        stoneRect = pygame.Rect(asteroidimgs[stone[2]].get_rect())
        stoneRect.left = stone[0]
        stoneRect.top = stone[1]
        if stoneRect.colliderect(spaceshipRect): # 돌이랑 우주선이랑 부딪혔다면
            asteroids.pop(index) # 부딪힌 행성 지워
            running = False

        screen.blit(asteroidimgs[stone[2]], (stone[0], stone[1]))
        index += 1

    pygame.display.flip()
    landingsound.play()

screen.blit(gameover, (0, 0))
showScore(score, screen.get_rect().centerx, screen.get_rect().centery, screen)
pygame.display.flip()

while True:
    fpsClock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)