# -----------------------------------------------------------------------------
# 36.8 연습문제: 리스트에 기능 추가하기
# -----------------------------------------------------------------------------
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


# -----------------------------------------------------------------------------
# 35.6 심사문제: 시간 클래스 만들기
# -----------------------------------------------------------------------------
class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))
