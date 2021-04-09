import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((480,640)) # 디스플레이 튜플 지정

FPS = 30
fpsClock = pygame.time.Clock() # 프로그램의 실행 속도를 조절

try:
    spaceshipimg = pygame.image.load("./img/spaceship.png")
    asteroid0 = pygame.image.load("./img/asteroid00.png")
    asteroid1 = pygame.image.load("./img/asteroid01.png")
    asteroid2 = pygame.image.load("./img/asteroid02.png")
    asteroidimgs = (asteroid0, asteroid1, asteroid2)

    gameover = pygame.image.load("./img/gameover.jpg")

    takeoffsound = pygame.mixer.Sound("./audio/takeoff.wav")
    landingsound = pygame.mixer.Sound("./audio/landing.wav")

    takeoffsound.play() # 음악 파일 재생


except Exception as err:
    print("그림 또는 효과음 삽입에 문제가 있습니다.", err)
    pygame.quit()
    sys.exit(0)


screen.fill((255, 255, 255)) # 색상 값을 매개변수로 튜플을 저장 rgb
screen.blit(spaceshipimg, (240, 600))
screen.blit(asteroidimgs[0], (240, 320))
pygame.display.flip() # 바꾼 색상을 적용시켜라
# 여기까지는 창이 떴다가 금방 사라짐

# 종료 버튼을 눌렀을 때 화면 꺼지기 (어떤 조건이 되기 전까지 반복적으로 그 화면을 띄워야 함)
while True:
    # 사양이 좋은 컴퓨터든 사양이 좋지 않은 컴퓨터든 일정한 속도로 게임을 즐기기 하기 위해서
    # while문의 속도를 조절
    # 1초에 30번 while문을 반복해라
    # 사양이 좋지 못한 컴퓨터가 1초에 10번밖에 반복하지 못한다면?
    # tick은 그냥 그렇게 두는 것
    fpsClock.tick(FPS)

    # while문 안에서 반복적으로 어떤 행동을 했는지 확인하겠다(화면 클릭, 스크롤 등등 이벤트를 얻어올 수 있음)
    # while문 안에서 반복적으로 어떤 행동을 했는지 확인하겠다(화면 클릭, 스크롤 등등 이벤트를 얻어올 수 있음)
    # 리스트 형태로 담아서 체크한다
    # 종ㅊㅇ료 버튼을 누르기 전까지 실행되어야 한다.
    for event in pygame.event.get():

        # 초당 프레임 수(FPS: 초당 while문이 얼마나 반복될지)를 조절해야한다
        # 종료버튼을 눌렀다면은
        if event.type == pygame.QUIT:
            # 종료해라
            pygame.quit() # 우리가 열었던 스크린을 닫아라
            sys.exit(0) # 프로그램을 종료시켜라

        landingsound.play()
