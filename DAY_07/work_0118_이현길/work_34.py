# -----------------------------------------------------------------------------
# 34.5 연습문제: 게임 캐릭터 클래스 만들기
# -----------------------------------------------------------------------------
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')


x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()


# -----------------------------------------------------------------------------
# 34.6 심사문제: 게임 캐릭터 클래스 만들기
# -----------------------------------------------------------------------------
class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print(f'티버: 피해량 {self.ability_power * 0.65 + 400}')

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
