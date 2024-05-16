import sys
import os
def mul(num, row):
    loop = 1
    for i in range(1, num+1):
        if (i % (row) == 0 or (i == num)):
            print('')
            for j in range(1, 10):
                for k in range(loop, i+1):
                    print("{: >3} X {: >3} = {: >3}".format(k, j, k*j), end='    ')
                print('')
            print('')
            loop += row
def enter():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')                #enter 함수의 코드가 다시 반복되기 전 콘솔 창 내용 모두 지우기
        try:
            n = (input("Enter a number : "))
            if n.lower() == "exit":                                     #EXIT 명령어
                sys.exit()
            elif int(n) <= 1 :                                          #출력하려는 숫자가 1이하일 때 오류 출력
                print("2보다 큰 단수를 입력하세요. (ENTER TO CONTINUE ... )")
                input()                                                 #엔터 입력 무한 대기
                continue                                                #코드 다시 반복
            elif int(n) >= 100 :                                        #출력하려는 숫자가 100 이상일 때 오류 출력
                print("100보다 작은 수를 입력하세요. (ENTER TO CONTINUE ... )")
                input()                                                 #엔터 입력 무한 대기
                continue
        except ValueError:                                              #모든 ValueError에 대해 오류 출력
            print("Invalid number, Try again. (ENTER TO CONTINUE ... )")
            input()                                                     #엔터 입력 무한 대기
            continue
        try:
            r = (input("Enter a row : "))
            if r.lower() == "exit":
                sys.exit()
            elif int(r) < 1:                                            #출력하려는 열의 수가 1보다 작을 때 모순이므로 오류 출력
                print("행은 1보다 커야 합니다. (ENTER TO CONTINUE ... )")
                input()                                                 #엔터 입력 무한 대기
            elif int(r) > int(n) :                                      #출력하려는 열의 수가 입력받은 수 보다 클때 모순이므로 오류 출력
                print("입력한 수보다 많은 행을 출력할 수 없습니다. (ENTER TO CONTINUE ... )")
                input()                                                 #엔터 입력 무한 대기
            else:
                return int(n), int(r)                                   #모든 값이 정상적일 때 반환
                break
        except ValueError:                                              #모든 ValueError에 대해 오류 출력
            print("Invalid number, Try again. (ENTER TO CONTINUE ... )")
            input()                                                     #엔터 입력 무한 대기
