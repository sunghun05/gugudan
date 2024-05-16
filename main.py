import forMul
import os
def menu() :
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')        #메뉴 함수의 코드가 다시 반복되기 전 콘솔 창 내용 모두 지우기
        print("{:=^100}".format("multiplication table mode"),end="\n\n\n")
        print("start gugudan ----> enter \"0\"", end="\n\n\n")
        print("{:-^100}".format("if you want to exit, enter \"exit\""), end="\n\n\n")

        try:
            m = (input("select menu number : "))
        except ValueError:                                      #변수가 NULL 일 때의 예외 처리
            print("invalid menu. Try again. (ENTER TO CONTINUE ... )")
            input()                                             #엔터 입력 무한 대기
            continue                                            #메뉴 함수 재실행

        try:
            if m.lower() == "exit":                             #EXIT 명령어
                break
            elif int(m) == 0:                                   #구구단 실행 메뉴
                data = forMul.enter()                           #forMul 모듈에서 enter함수의 반환값을 data 리스트에 저장
                forMul.mul(data[0], data[1])
                break
            else:
                print("enter the valid menu number (ENTER TO CONTINUE ... )")
                input()                                         #엔터 입력 무한 대기
                continue                                        #메뉴 함수 재실행
        except ValueError:                                      #모든 ValueError에 대해 오류 출력
            print("invalid menu. Try again. (ENTER TO CONTINUE ... )")
            input()                                             #엔터 입력 무한 대기
            continue                                            #메뉴 함수 재실행

if __name__ == "__main__":
    menu()