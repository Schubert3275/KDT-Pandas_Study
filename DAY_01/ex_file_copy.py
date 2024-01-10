# -----------------------------------------------------------------------------
# 파일을 하나 선택 후 복사본 파일 생성 하기
# - 예) message.txt ====> message_copy.txt
# -----------------------------------------------------------------------------
filename = 'message.txt'

# 원본 파일 내용 읽은 후 저장
with open(filename, mode='r', encoding='utf-8') as f:
    data = f.read()

filename2 = 'message_copy.txt'

# 복사본 파일에 내용 쓰기
with open(filename2, mode='w', encoding='utf-8') as f:
    f.write(data)


with open(filename, mode='r', encoding='utf-8') as of:
    with open(filename2, mode='w', encoding='utf-8') as nf:
        nf.write(of.read())
