from telebot.async_telebot import AsyncTeleBot
import asyncio



bot = AsyncTeleBot("6776179983:AAFn7UFsENsC6kSutnpZEqn03ghKXTQuRt4")

@bot.message_handler()
async def echo_all(message):
    await bot.reply_to(message, "Я не понимаю.")

async def send_message(user_id, detail: str):
    await bot.send_message(user_id, f'{detail}')

async def main():
    # Запуск бота
    print("Бот запущен...")
    await bot.polling()

if __name__ == '__main__':
    asyncio.run(main())
