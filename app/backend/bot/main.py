from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio



bot = AsyncTeleBot("7542158551:AAHHSc6oxVp91XPB7TSb2NdE2lGaE7Jtduo")


@bot.message_handler()
async def send_welcome(message):
    # Создание инлайн-клавиатуры
    markup = InlineKeyboardMarkup()

    # Первая кнопка: Открыть сайт
    button_site = InlineKeyboardButton("Играть в 1 клик🎲", web_app=WebAppInfo(url="https://locfront.ru.tuna.am"))
    
    # Вторая кнопка: Перейти на Телеграм-канал
    button_channel = InlineKeyboardButton("Подписаться на канал", url="https://t.me/klinning63")
    
    # Третья кнопка: Отправить другое сообщение
    button_message = InlineKeyboardButton("Правила и призы", callback_data="send_another_message")

    # Добавляем кнопки в разметку
    markup.add(button_site)
    markup.add(button_channel)
    markup.add(button_message)

    # Отправляем сообщение с кнопками
    await bot.send_message(message.chat.id, "Вы на верном пути, нажмите «Играть» и следуйте подсказкам!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "send_another_message")
async def callback_query(call):
    # Отправка другого сообщения
    await bot.send_message(call.message.chat.id, 
                     """
🎁ПРИЗЫ🎁
🥇Бесплатная уборка участка (до 7 соток)
🥇Снегоуборочная машина
🥇Газонокосилка 
🥇Электропила
🥇Бензопила
🥇Триммер
🥇Сучкорез электрический
🥇Аккумуляторная пила
🥇Воздуходувка бензиновая
🥇Воздуходувка электрическая
🥇Шуруповерт
🥇УШМ
🥇20.000 рублей
🥇10.000 рублей
🥇Набор ключей

🥈Бесплатная уборка снега (до 7 соток)
🥈Вывоз мусора на большой Газели 
🥈Вывоз мусора на большой Газели с грузчиками
🥈Услуги грузчиков на 2 часа
🥈Уборка 55% участка
🥈Уборка 40% участка
🥈Биокамин
🥈40 литров бензина
🥈500 рублей 
🥈Вилы
🥈Топор
🥈Сучкорез
🥈Мотыга
🥈Грабли
🥈Лопата
🥈Фирменный секатор
🥈Цепь на пилу

🥉Грабли веерные
🥉Корнеудалитель
🥉Услуги грузчиков на 1 час
🥉Вывоз мусора на малой Газели
🥉Садовые ножницы
🥉Садовый секатор
🥉50 рублей на телефон
🥉100 рублей на телефон
🥉Скидка на все виды услуг 5%
🥉Скидка на все виды услуг 7%
🥉Скидка на все виды услуг 9%
🥉Скидка на все виды услуг 11%
🥉Скидка на все виды услуг 15%
🥉Скидка на все виды услуг 17%

Список призов может редактироваться и дополняться.

Правила:
1. Призы, предусмотренные данной онлайн-игрой, могут быть получены и использованы только при наличии у участника действующей подписки на наш телеграмм канал (не менее 3х дней, до получения приза);
2. В онлайн-игре «Рулетка» нельзя докупить попытку или поменять приз;
3. Крутить рулетку можно 1 раз в 24 часа.
"""
                     )


async def send_message(user_id, detail: str):
    await bot.send_message(user_id, f'{detail}')

async def main():
    await bot.polling()

if __name__ == '__main__':
    asyncio.run(main())
