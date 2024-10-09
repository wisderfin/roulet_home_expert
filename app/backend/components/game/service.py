from random import choices
from components.game.utils import get_all_presents
from components.redis_utils import get, set

async def get_present(sum: int):
    # Получаем текущее значение "profit" из Redis
    profit = get('profit')
    if profit is None or int(profit) < 0:
        profit = sum
    else:
        profit = int(profit) + sum
    set('profit', profit)

    # Обновляем сумму всех ставок
    total_bets = get('total_bets')
    if total_bets is None:
        total_bets = sum
    else:
        total_bets = int(total_bets) + sum
    set('total_bets', total_bets)

    # Получаем все доступные подарки
    presents = await get_all_presents()

    # Фильтрация подарков на основе их цены
    # Цена подарка должна быть меньше текущей прибыли минус 10% и больше 1/4 суммы ставки
    suitable_presents = list(filter(lambda x: x.price < profit - profit // 10 and x.price > sum // 4, presents))


    # Рассчитываем вес для каждого подарка на основе ставки (sum)
    weights = []
    for present in suitable_presents:
        if present.price <= sum // 2:
            weights.append(0.6)  # Дешевые подарки — высокая вероятность
        elif present.price <= sum + sum // 5:
            weights.append(0.35)  # Средние подарки — средняя вероятность
        else:
            weights.append(0.05)  # Дорогие подарки — низкая вероятность

    # Проверяем текущую прибыль казино для контроля над крупными выигрышами
    if profit > sum * 10:
        # Если прибыль высокая, увеличиваем вероятность крупного выигрыша
        for i, present in enumerate(suitable_presents):
            if present.price > sum:
                weights[i] *= 1.5  # Увеличиваем шансы дорогих подарков

    # Выбираем выигрышный подарок с учетом весов
    winning_present = choices(suitable_presents, weights=weights, k=1)[0]

    # Ограничение крупного выигрыша: если подарок превышает сумму ставки
    if winning_present.price > sum and profit < sum * 5:
        # Если прибыль недостаточна для крупного выигрыша, выбираем другой подарок
        profit = 0  # Обнуляем прибыль для контроля
        set('profit', profit)
        winning_present = choices([p for p in suitable_presents if p.price <= sum * 2.5], k=1)[0]

    # Убираем выигрышный подарок из списка для невыигрышных элементов
    remaining_presents = [p for p in suitable_presents if p != winning_present]

    # Если недостаточно подарков для 20 элементов, заполняем случайными подарками
    if len(remaining_presents) < 20:
        remaining_presents += choices(presents, k=20 - len(remaining_presents))

    # Выбираем 20 случайных невыигрышных подарков
    non_winning_presents = choices(remaining_presents, k=20)

    # Вставляем выигрышный подарок в случайное место
    results = non_winning_presents[:]
    results.insert(19, winning_present)

    # Обновляем "profit", уменьшая его на стоимость выигрышного подарка
    profit -= winning_present.price
    set('profit', profit)

    # Обновляем сумму выданных призов
    total_prizes = get('total_prizes')
    if total_prizes is None:
        total_prizes = winning_present.price
    else:
        total_prizes = int(total_prizes) + winning_present.price
    set('total_prizes', total_prizes)
    # Возвращаем список, выигрыш и текущую прибыль казино
    total_profit = total_bets - total_prizes
    return   ['+'] + [p.name for p in results[1:]]
