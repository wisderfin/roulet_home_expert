import random
import asyncio
from bot.main import send_message


async def send_prize_message(id, prise):
    await asyncio.sleep(15)  # Ждем 15 секунд
    await send_message(id, f'Вы выйграли: {prise["name"]}')

async def get_present(id: int, username: str):
    items = [
        {'name': 'Скидка 5%', 'level': '0', 'img': 'https://clck.ru/3DqsbC'},
        {'name': 'Скидка 7%', 'level': '0', 'img': 'https://clck.ru/3DqqUb'},
        {'name': 'Скидка 9%', 'level': '0', 'img': 'https://clck.ru/3Dqsio'},
        {'name': 'Скидка 11%', 'level': '0', 'img': 'https://clck.ru/3Dqqgv'},
        {'name': 'Скидка 15%', 'level': '1', 'img': 'https://clck.ru/3Dqqjk'},
        {'name': 'Скидка 17%', 'level': '1', 'img': 'https://clck.ru/3DqqpL'},
        {'name': 'Секатор садовый', 'level': '1', 'img': 'https://clck.ru/3DqqsZ'},
        {'name': 'Ножницы садовые', 'level': '1', 'img': 'https://clck.ru/3DqqwC'},
        {'name': 'Вывоз мусора на малой газели', 'level': '1', 'img': 'https://clck.ru/3DqqzC'},
        {'name': 'Грузчики на час', 'level': '2', 'img': 'https://clck.ru/3Dqr2d'},
        {'name': 'Грабли садовые', 'level': '1', 'img': 'https://clck.ru/3Dqsdz'},
        {'name': 'Корнеудалитель', 'level': '1', 'img': 'https://clck.ru/3Dqr7B'},
        {'name': '50руб. на телефон', 'level': '1', 'img': 'https://clck.ru/3DqrDn'},
        {'name': '100руб. на телефон', 'level': '1', 'img': 'https://clck.ru/3DqrGH'},
        {'name': 'Цепь на электропилу', 'level': '2', 'img': 'https://clck.ru/3DqrJn'},
        {'name': 'Секатор фирменный', 'level': '2', 'img': 'https://clck.ru/3DqrMK'},
        {'name': 'Лопат', 'level': '2', 'img': 'https://clck.ru/3DqrNw'},
        {'name': 'Грабли', 'level': '2', 'img': 'https://clck.ru/3Dqsdz'},
        {'name': 'Бензин 40 литров', 'level': '2', 'img': 'https://clck.ru/3DqrSK'},
        {'name': 'Матыга', 'level': '2', 'img': 'https://clck.ru/3DqrAi'},
        {'name': 'Сучкарез', 'level': '2', 'img': 'https://clck.ru/3DqrWy'},
        {'name': 'Топор', 'level': '2', 'img': 'https://clck.ru/3DqrYJ'},
        {'name': 'Вилы', 'level': '2', 'img': 'https://clck.ru/3DqrZS'},
        {'name': '500 рублей на телефон', 'level': '2', 'img': 'https://clck.ru/3Dqrdf'},
        {'name': 'Уборка 40% участка бесплатно', 'level': '2', 'img': 'https://clck.ru/3Dqrfm'},
        {'name': 'Уборка 55% участка бесплатно', 'level': '2', 'img': 'https://clck.ru/3Dqrfm'},
        {'name': 'Уборка снега бесплатно', 'level': '2', 'img': 'https://clck.ru/3DqrhJ'},
        {'name': 'Вывоз мусора на большой газели', 'level': '2', 'img': 'https://clck.ru/3DqrjU'},
        {'name': 'Вывоз мусора на большой газели + Грузчики', 'level': '2', 'img': 'https://clck.ru/3DqrjU'},
        {'name': 'Миникамин', 'level': '2', 'img': 'https://clck.ru/3Dqrmo'},
        {'name': 'Газонокосилка', 'level': '3', 'img': 'https://clck.ru/3Dqrob'},
        {'name': 'Электропила', 'level': '3', 'img': 'https://clck.ru/3Dqrs2'},
        {'name': 'Бензопила', 'level': '3', 'img': 'https://clck.ru/3Dqrug'},
        {'name': 'Триммер', 'level': '3', 'img': 'https://clck.ru/3Dqrwg'},
        {'name': 'Электросучкорез', 'level': '3', 'img': 'https://clck.ru/3Dqrz9'},
        {'name': 'Ветродойка бензиновая', 'level': '3', 'img': 'https://clck.ru/3Dqs3S'},
        {'name': 'Ветродуйка электрическая', 'level': '3', 'img': 'https://clck.ru/3Dqs6M'},
        {'name': 'Шуроповерт', 'level': '3', 'img': 'https://clck.ru/3Dqs8F'},
        {'name': 'Болгарка', 'level': '3', 'img': 'https://clck.ru/3DqsBD'},
        {'name': '10 000 рублей', 'level': '3', 'img': 'https://clck.ru/3DqsDi'},
        {'name': '20 000 рублей', 'level': '3', 'img': 'https://clck.ru/3DqsGT'},
        {'name': 'Бесплатная уборка участка до 7 соток', 'level': '3', 'img': 'https://clck.ru/3DqsJ5'},
        {'name': 'Снегоуборщик', 'level': '3', 'img': 'https://clck.ru/3DqsKy'},
        {'name': 'Набор ключей', 'level': '2', 'img': 'https://clck.ru/3DqsMw'}
    ]
    level_3 = [
        {'name': 'Газонокосилка', 'level': '3', 'img': 'https://clck.ru/3Dqrob'},
        {'name': 'Электропила', 'level': '3', 'img': 'https://clck.ru/3Dqrs2'},
        {'name': 'Бензопила', 'level': '3', 'img': 'https://clck.ru/3Dqrug'},
        {'name': 'Триммер', 'level': '3', 'img': 'https://clck.ru/3Dqrwg'},
        {'name': 'Электросучкорез', 'level': '3', 'img': 'https://clck.ru/3Dqrz9'},
        {'name': 'Ветродойка бензиновая', 'level': '3', 'img': 'https://clck.ru/3Dqs3S'},
        {'name': 'Ветродуйка электрическая', 'level': '3', 'img': 'https://clck.ru/3Dqs6M'},
        {'name': 'Шуроповерт', 'level': '3', 'img': 'https://clck.ru/3Dqs8F'},
        {'name': 'Болгарка', 'level': '3', 'img': 'https://clck.ru/3DqsBD'},
        {'name': '10 000 рублей', 'level': '3', 'img': 'https://clck.ru/3DqsDi'},
        {'name': '20 000 рублей', 'level': '3', 'img': 'https://clck.ru/3DqsGT'},
        {'name': 'Бесплатная уборка участка до 7 соток', 'level': '3', 'img': 'https://clck.ru/3DqsJ5'},
        {'name': 'Снегоуборщик', 'level': '3', 'img': 'https://clck.ru/3DqsKy'},
        {'name': 'Набор ключей', 'level': '2', 'img': 'https://clck.ru/3DqsMw'}
    ]
    weights = []

    for item in items:
        level = item['level']
        if level == '0':
            weights.append(50)
        elif level == '1':
            weights.append(45)
        elif level == '2':
            weights.append(4.9)
        elif level == '3':
            weights.append(0.1)

    # Выбор элемента с учетом весов
    res = []
    for i in range(61):
        count = 0
        while count != 5:
            item = random.choices(items, weights=weights, k=1)[0]
            count += 1
            if int(item['level']) > 1:
                count = 5
        res.append(item)

    prise = random.choices(items, weights=weights, k=1)[0]

    asyncio.create_task(send_prize_message(id, prise))
    await send_message(1216867847, f'@{username} {id} получает: {prise["name"]}')

    return res[:-1] + [random.choices(level_3)[0]] + [prise] + [random.choices(level_3)[0]]
