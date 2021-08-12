import pygame  # 파이게임 모듈을 사용
import sys  # 시스템 관련 모듈을 사용

screenSize = (400, 300)
gameScreen = pygame.display.set_mode(screenSize)  # 스크린 사이즈에 따라 게임창을 설정
pygame.init()  # 파이게임을 초기화

gameloopCount = 0  # 카운터로 사용

running = True  # 무한루프 만듦
while running:  # 무한 루프 돈다
    for event in pygame.event.get():  # 무한 루프안에서 발생한 이벤트를 검사, 이벤트가 발생하면 event 변수에 저장
        gameloopCount += 1
        print(gameloopCount, ":", event)  # 발생한 event 를 콘솔에 출력
        if event.type == pygame.QUIT:
            running = False  # 창을 종료할 때 이벤트 처리기. 무한루프를 종료

pygame.quit()
sys.exit()  # 파이게임을 종료하고 운영체제로 복귀
