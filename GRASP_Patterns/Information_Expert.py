# пример: Расчет урона персонажа в той же самой игре Dark Souls

# класс, в котором известны все характеристики
class DeepDarkFantasyFun:
    hp = 100
    strength = 1
    agility = 1

    ## Правильно
    # Функция подсчета урона. Так как наш герой содержит все характеристики,
    # которые используются при подсчете силы атаки,
    # правильнее будет реализовать это внутри класса, не делегируя это какому то другому классу
    def attack(self) -> int:
        attack_power = self.strength*3 + self.agility*2.5
        return attack_power



# Не правильно
class AttackPowerCounter:

    def attack(self, hero: DeepDarkFantasyFun) -> int:
        attack_power = hero.strength*3 + hero.agility*2.5
        return attack_power


def main():
    hero = DeepDarkFantasyFun()
    hero.attack()

    hero2 = DeepDarkFantasyFun()
    AttackPowerCounter().attack(hero2)


if __name__ == '__main__':
    main()