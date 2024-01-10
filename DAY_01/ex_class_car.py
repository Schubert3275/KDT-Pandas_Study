# ---------------------------------------------------------------------------------------
# 자동차 관리 프로그램 만들기
# - 엔진, 연료, 브랜드, 색상, 번호
# 전진, 후진 좌회전, 정지
# ---------------------------------------------------------------------------------------
# engine = '휘발유엔진'
# food = '휘발유'
# marker = '현대'
# color = '흰색'
# number = '111가1111'
#
# engine2 = '휘발유엔진'
# food2 = '휘발유'
# marker2 = '현대'
# color2 = '흰색'
# number2 = '111가2222'
#
# engine3 = '휘발유엔진'
# food3 = '휘발유'
# marker3 = '기아'
# color3 = '회색'
# number3 = '111가3333'
#
#
# def go(number): print(f'{number} 자동차가 전진')
# def back(number): print(f'{number} 자동차가 후진')
# def left_go(number): print(f'{number} 자동차가 좌회전')
# def right_go(number): print(f'{number} 자동차가 우회전')
# def stop(number): print(f'{number} 자동차가 정지')
#
#
# carDict = {'111가1111': {'engine': '휘발유엔진', 'color': '흰색', 'maker': '현대', 'autodrive': False},
#            '111가2222': {'engine': '휘발유엔진', 'color': '흰색', 'maker': '기아', 'autodrive': False},
#            '111가3333': {'engine': '경유엔진', 'color': '녹색', 'maker': '현대', 'autodrive': True}}
# # 자동차 관리 -------------------------------------------------
# for k, v in carDict.items():
#     print(f' 판매 차량 [{number}]')
#     for suvK, subV in v.items():
#         print(f'- {suvK} : [{subV}]')

# ---------------------------------------------------------------------------------------
# 자동차 클래스
# - 역할 : 자동차 관련 데이터와 기능을 모두 저장 관리 클래스
# - 문법
#   class 클래스명:
#   <--> 코드
# ---------------------------------------------------------------------------------------
class Car:
    maker = '현대'

    # 클래스 생성 시 필수로 사용되는 메서드
    # 힙 메모리에 속성들의 값을 저장해주는 역할
    def __init__(self, engine_, food_, color_, number_):
        print('__init__')
        # 자동차 클래스가 가지는 속성 메모리 힙에 저장
        self.engine = engine_
        self.maker = food_
        self.color = color_
        self.number = number_

    # 자동차의 기능 => 함수형식
    def go(self):
        print(f'{self.number} 자동차 전진')

    def back(self):
        print(f'{self.number} 자동차 후진')

    def stop(self):
        print(f'{self.number} 자동차 정지')


# 클래스로 자동차 객체 생성 ------------------------------------------------------------
myCar = Car('휘발유엔진', '휘발유', '흰색', '111가1111')
myCar2 = Car('휘발유엔진', '휘발유', '핫핑크색', '111가7777')
