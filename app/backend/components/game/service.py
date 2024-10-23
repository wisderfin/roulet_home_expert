import random
import asyncio
from bot.main import send_message


# async def send_prize_message(id, prise):
#     await asyncio.sleep(15)  # Ждем 15 секунд
#     await send_message(id, f'Вы выйграли: {prise["name"]}')

async def get_present(id: int, username: str):
    items = [
        {'name': 'Скидка 5%', 'level': '0', 'img': '5proc.jpg'},
        {'name': 'Скидка 7%', 'level': '0', 'img': '7proc.jpg'},
        {'name': 'Скидка 9%', 'level': '0', 'img': '9proc.jpg'},
        {'name': 'Скидка 11%', 'level': '0', 'img': '11proc.jpg'},
        {'name': 'Скидка 15%', 'level': '1', 'img': '15proc.jpg'},
        {'name': 'Скидка 17%', 'level': '1', 'img': '17proc.jpg'},
        {'name': 'Секатор садовый', 'level': '1', 'img': 'secator.jpg'},
        {'name': 'Ножницы садовые', 'level': '1', 'img': 'sesisers.jpg'},
        {'name': 'Вывоз мусора на малой газели', 'level': '1', 'img': 'musor.jpg'},
        {'name': 'Грузчики на час', 'level': '2', 'img': 'gruzOnhours.jpg'},
        {'name': 'Грабли садовые', 'level': '1', 'img': 'grabSad.jpg'},
        {'name': 'Корнеудалитель', 'level': '1', 'img': 'korneDelete.jpg'},
        {'name': '50руб. на телефон', 'level': '1', 'img': '50RUB.jpg'},
        {'name': '100руб. на телефон', 'level': '1', 'img': '100RUB.jpg'},
        {'name': 'Цепь на электропилу', 'level': '2', 'img': 'chain.jpg'},
        {'name': 'Секатор фирменный', 'level': '2', 'img': 'SekatorFirmenniy.jpg'},
        {'name': 'Лопата', 'level': '2', 'img': 'Lopata.jpg'},
        {'name': 'Грабли', 'level': '2', 'img': 'grab.jpg'},
        {'name': 'Матыга', 'level': '2', 'img': 'motga.jpg'},
        {'name': 'Сучкарез', 'level': '2', 'img': 'suckres.jpg'},
        {'name': 'Топор', 'level': '2', 'img': 'topor.jpg'},
        {'name': 'Вилы', 'level': '2', 'img': 'Vily.jpg'},
        {'name': '500 рублей на телефон', 'level': '2', 'img': '500RUB.jpg'},
        {'name': 'Уборка 40% участка бесплатно', 'level': '2', 'img': '40terr.jpg'},
        {'name': 'Уборка 55% участка бесплатно', 'level': '2', 'img': '55terr.jpg'},
        {'name': 'Уборка снега бесплатно', 'level': '2', 'img': 'sneg.jpg'},
        {'name': 'Вывоз мусора на большой газели', 'level': '2', 'img': 'musor.jpg'},
        {'name': 'Вывоз мусора на большой газели + Грузчики', 'level': '2', 'img': 'gruzAnddazel.jpg'},
        {'name': 'Миникамин', 'level': '2', 'img': 'Kamin.jpg'},
        {'name': 'Газонокосилка', 'level': '3', 'img': 'gazon.jpg'},
        {'name': 'Бензин 40 литров', 'level': '3', 'img': '40litr.jpg'},
        {'name': 'Электропила', 'level': '3', 'img': 'elPila.jpg'},
        {'name': 'Бензопила', 'level': '3', 'img': 'Benzopila.jpg'},
        {'name': 'Триммер', 'level': '3', 'img': 'Trimer.jpg'},
        {'name': 'Электросучкорез', 'level': '3', 'img': 'Elektrosu4korez.jpg'},
        {'name': 'Ветродойка бензиновая', 'level': '3', 'img': 'BenzoDuika.jpg'},
        {'name': 'Ветродуйка электрическая', 'level': '3', 'img': 'Elektroduika.jpg'},
        {'name': 'Шуроповерт', 'level': '3', 'img': 'Drel.jpg'},
        {'name': 'Болгарка', 'level': '3', 'img': 'Bolgarka.jpg'},
        {'name': '10 000 рублей', 'level': '3', 'img': '10k.jpg'},
        {'name': '20 000 рублей', 'level': '3', 'img': '20k.jpg'},
        {'name': 'Бесплатная уборка участка до 7 соток', 'level': '3', 'img': '7sotok.jpg'},
        {'name': 'Снегоуборщик', 'level': '3', 'img': 'UborkaSnega.jpg'}, 
        {'name': 'Набор ключей', 'level': '3', 'img': 'NaborInstrumentov.jpg'} 
    ]
    level_3 = [
        {'name': 'Газонокосилка', 'level': '3', 'img': 'gazon.jpg'},
        {'name': 'Бензин 40 литров', 'level': '3', 'img': '40litr.jpg'},
        {'name': 'Электропила', 'level': '3', 'img': 'elPila.jpg'},
        {'name': 'Триммер', 'level': '3', 'img': 'Trimer.jpg'},
        {'name': 'Электросучкорез', 'level': '3', 'img': 'Elektrosu4korez.jpg'},
        {'name': 'Ветродойка бензиновая', 'level': '3', 'img': 'BenzoDuika.jpg'},
        {'name': 'Ветродуйка электрическая', 'level': '3', 'img': 'Elektroduika.jpg'},
        {'name': 'Шуроповерт', 'level': '3', 'img': 'Drel.jpg'},
        {'name': 'Болгарка', 'level': '3', 'img': 'Bolgarka.jpg'},
        {'name': '10 000 рублей', 'level': '3', 'img': '10k.jpg'},
        {'name': '20 000 рублей', 'level': '3', 'img': '20k.jpg'},
        {'name': 'Бесплатная уборка участка до 7 соток', 'level': '3', 'img': '7sotok.jpg'},
        {'name': 'Снегоуборщик', 'level': '3', 'img': 'UborkaSnega.jpg'},
        {'name': 'Набор ключей', 'level': '3', 'img': 'NaborInstrumentov.jpg'}
    ]
    weights = []

    for item in items:
        level = item['level']
        if level == '0':
            weights.append(70)
        elif level == '1':
            weights.append(19)
        elif level == '2':
            weights.append(0.9)
        elif level == '3':
            weights.append(0.1)

    prise = random.choices(items, weights=weights, k=1)[0]


    weights = []
    for item in items:
        level = item['level']
        if level == '0':
            weights.append(10)
        elif level == '1':
            weights.append(20)
        elif level == '2':
            weights.append(40)
        elif level == '3':
            weights.append(30)
    res = []
    for i in range(61):
        item = random.choices(items, weights=weights, k=1)[0]
        res.append(item)


    # asyncio.create_task(send_prize_message(id, prise))
    # 6109323456
    # 1216867847 твой
    await send_message(6109323456, f'@{username} получает: {prise["name"]}')

    return res[:-1] + [random.choices(level_3)[0]] + [prise] + [random.choices(level_3)[0]]
