# Параметры классов - интеллект, здоровье, красноречие, репутация
PLAYER_CLASSES = {
            'Ботан': [35, -10, -10, 0],
            'Спортсмен': [-5, 30, -10, 0],
            'Поэт': [5, -10, 20, 0],
            'Человек': [5, 5, 5, 0]
        }


class Player:
    def __init__(self, player_name, player_class):
        self.player_class = player_class
        self.player_name = player_name
        self.params = PLAYER_CLASSES[player_class]

    def intelligence(self, delta):
        self.params[0] += delta
        return (f'Ваш интеллект изменен на {delta} \n'
                f'Новое значение  {self.params[0]}')

    def health(self, delta):
        self.params[1] += delta
        return (f'Ваше здоровье изменено на {delta} \n'
                f'Новое значение  {self.params[1]}')

    def eloquence(self, delta):
        self.params[2] += delta
        return (f'Ваше красноречие изменено на {delta} \n'
                f'Новое значение  {self.params[2]}')

    def rep(self, delta):
        self.params[3] += delta
        return (f'Ваша репутация изменена на {delta} \n'
                f'Новое значение  {self.params[3]}')





