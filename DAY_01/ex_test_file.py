# -----------------------------------------------------------------------------
# 입력받은 내용을 파일에 저장하는 프로그램
# - 조건: 'X', 'x' 입력 시 입력 받기 중단
# -----------------------------------------------------------------------------
# 모듈 로딩 -------------------------------------------------------------------
import time
from datetime import date, datetime

today = date.today()
print(today.year, today.month, today.day)

print(today)
print(today.strftime("%d/%m/%y"))
print(today.strftime("%y/%m/%d"))

# today2 = datetime
# print(today2.year, today2.month, today2.day, today2.hour, today2.minute, today2.second)

# 관련 변수 -------------------------------------------------------------------
filename = 'test.txt'

# print(time.time())
# print(time.localtime())
# print(time.ctime(time.time()))

# 프로그램 기능 구현 부분 -----------------------------------------------------
with open(filename, mode='a', encoding='utf-8') as f:
    while True:
        data = input("메시지 입력 (종료-X, x) : ")
        # 종료 검사
        if data in ('X', 'x'):
            print("종료합니다.")
            break  # 즉시 종료로 while 문에서 아래 코드 실행 안됨!

        # 파일에 쓰기 즉 저장
        f.write(data+'\n')

        # 일정 시간 일시정지 후 반복하기
        time.sleep(0.1)

    # 종료 시간을 파일에 기록
    f.write(f'저장 시간 : {today.strftime("%y/%m/%d")}\n')
