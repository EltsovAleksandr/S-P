l = ['R', 'P', 'S']  # P - бумага, S - ножницы, R - камень
class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(a):
    if len(a) != 2:
        raise WrongNumberOfPlayersError ('Кол-во игроков должно быть 2')
        # return ('WrongNumberOfPlayersError')
    elif a[0][1] not in l or a[1][1] not in l:
        raise NoSuchStrategyError ('Неправильный ход')
        # return 'NoSuchStrategyError'
    elif a[0][1] == a[1][1]:
        return f'{a[0][0]} {a[0][1]}'
    elif a[0][1].upper() == 'P':  # первый игрок бумага
        if a[1][1].upper() == 'S':  # второй игрок ножницы
            return f'{a[1][0]} {a[1][1]}'
        else:
            return f'{a[0][0]} {a[0][1]}'
    elif a[0][1].upper() == 'S':  # перый игрок ножницы
        if a[1][1].upper() == 'R':  # второй игрок камень
            return f'{a[1][0]} {a[1][1]}'
        return f'{a[0][0]} {a[0][1]}'
    elif a[0][1].upper() == 'R':  # первый игрок камень
        if a[1][1].upper() == 'P':  # второй игрок бумага
            return f'{a[1][0]} {a[1][1]}'
        return f'{a[0][0]} {a[0][1]}'

