import turtle as t
import random
import time
import os

def message(str_up, str_down): # 위아래로 메시지 출력
    player.goto(0,100)
    player.write(str_up, False, "center", ("Arial", 20, "bold")) # Arial 폰트, 폰트 크기 20, 굵게, 가운데 정렬로 str_up 작성
    player.goto(0,-100)
    player.write(str_down, False, "center", ("Arial", 15, "normal"))
    player.home() # 거북이 원점으로 이동
    player.showturtle()

def start(): # 게임 시작
    playing = True
    player.clear()
    playing = play(playing)
    end(playing)

def play(playing): # 게임 진행
    max_time = time.time() + 20 # 최대 20초의 시간 제한

    while playing:
        if time.time() > max_time:
            playing = False
            return playing
        player.showturtle()
        player.up() # 펜 들기
        location = random.choice(location_list)
        player.goto(location)
        time.sleep(random.uniform(0.1, 1)) # 거북이가 나타나는 시간을 0.1초에서 1초 사이 랜덤으로 지연

def show_score(score): # 점수 출력
    score_board.clear()
    score_board.color("white")
    score_board.goto(150, 150)
    score_board.pencolor("black")
    score_board.write("Score : %d" % score, False, "left", ("Arial", 13, "bold"))
    score_board.color("white")

def right():  # 유저가 누른 방향키가 오른쪽이면 점수 획득
    global score
    if player.position() == (200.00, 0.00):  # 거북이의 위치가 오른쪽이면
        player.hideturtle()
        score = score + 1
        show_score(score)

def left():  # 유저가 누른 방향키가 왼쪽이면 점수 획득
    global score
    if player.position() == (-200.00, 0.00):  # 거북이의 위치가 왼쪽이면
        player.hideturtle()
        score = score + 1
        show_score(score)

def up():  # 유저가 누른 방향키가 위쪽이면 점수 획득
    global score
    if player.position() == (0.00, 200.00):  # 거북이의 위치가 위쪽이면
        player.hideturtle()
        score = score + 1
        show_score(score)

def down():  # 유저가 누른 방향키가 아래쪽이면 점수 획득
    global score
    if player.position() == (0.00, -200.00):  # 거북이의 위치가 아래쪽이면
        player.hideturtle()
        score = score + 1
        show_score(score)

def end(playing): # 게임 종료
    global score
    if not playing:
        score_board.clear()
        text = "Score : %d" % score
        message("Game Over", text) # 게임 종료 화면으로 "Game Over"와 점수를 출력
        score = 0

player = t.Turtle() # 거북이 객체 생성
player.shape("turtle")
player.speed(0)
player.up()

screen = t.Screen() # screen 객체 생성
screen.title("Catch Turtle") # 그래픽 창 이름 지정
screen.setup(500, 500) # 창 크기 500*500으로 설정

score_board = t.Turtle() # 점수판 객체 생성
score_board.color("white")
score_board.goto(150,150)

score = 0

location_list = [(0,200), (0,-200), (200,0), (-200,0)] # 거북이의 위치(위, 아래, 오른쪽, 왼쪽) 리스트로 생성

screen.onkeypress(start, "space") # 스페이스 바를 누르면 start 함수 실행
screen.onkeypress(right, "Right") # 오른쪽 키를 누르면 right 함수 실행
screen.onkeypress(left, "Left")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.listen() # 이 명령어를 실행시켜야 키 입력모드가 실행되어 입력된 키에 반응

message("Catch Turtle", "[Space]") # 게임 시작하기 전 첫 화면으로 "Catch Turtle"과 "[Space]"를 출력

os.system('pause')