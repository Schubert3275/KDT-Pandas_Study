# -----------------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -----------------------------------------------------------------------------
filename = 'message.txt'

with open(filename, mode='r', encoding='utf-8') as f:
    f.seek(5)  # byte 단위로 이동
    print(f.read(30))
    print(f'현재 위치 : {f.tell()}')  # byte 단위로 위치 반환
    print(f.name, f.closed)

    f.seek(0)
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')

print(f.name, f.closed)
