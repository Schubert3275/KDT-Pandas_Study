# -----------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(Read)
# - 사용 내장 함수 : open()
# -----------------------------------------------------------------------------
# (1) open
file = open('message.txt', encoding='utf8')
print(f'file => {type(file)}, {file}')

# (2) IO => read() : 파일 안에 모든 내용 다 읽어오기
# fdata = file.read()
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기
# fdata = file.read(5)  # 지정된 숫자 만큼 문자 읽기
# print(f'fdata => {type(fdata)}, {fdata}')
#
# fdata = file.read(5)
# print(f'fdata => {type(fdata)}, {fdata}')

# (2) IO => readline() : '\n' 기준으로 한 줄 읽어오기
# datas = []
# while True:
#     fline = file.readline()
#     if not fline:
#         break
#     print(f'fline => {type(fline)}, {fline}', end='')
#     datas.append(fline)

# (2) IO => readlines() : '\n' 기준으로 한 줄 씩 읽은 것을 리스트에 담아서 반환
datas = file.readlines()

print(datas)
# (3) close
file.close()
