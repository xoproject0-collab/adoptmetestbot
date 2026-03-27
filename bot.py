from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from apscheduler.schedulers.background import BackgroundScheduler
from parser import update_values
import json

TOKEN = "8739109558:AAG_EapMhXyjczhkoe44Gb7x1SKjeMLhG0A"  # <-- вставь сюда свой токен

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

pets_selected = []
def make_keyboard(options):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for o in options:
        kb.add(KeyboardButton(o))
    return kb

# Кнопки для выбора питомцев
def make_keyboard(options):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for o in options:
        kb.add(KeyboardButton(o))
    return kb

# Стартовая команда
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот-калькулятор Adopt Me.\nИспользуй /add, чтобы выбрать питомца для сравнения.")

# Добавление питомца
@dp.message_handler(commands=["add"])
async def add(message: types.Message):
    with open("values.json", encoding="utf-8") as f:
        data = json.load(f)
    kb = make_keyboard(list(data.keys()))
    await message.answer("Выбери питомца:", reply_markup=kb)

# Обработка выбора питомца и сравнение
@dp.message_handler()
async def choose_pet(message: types.Message):
    global pets_selected
    with open("values.json", encoding="utf-8") as f:
        data = json.load(f)

    if message.text not in data:
        await message.answer("Такого питомца нет. Попробуй ещё раз.")
        return

    pets_selected.append(message.text)
    await message.answer(f"{message.text} добавлен!")

    if len(pets_selected) == 2:
        first, second = pets_selected
        if data[first] > data[second]:
            winner = first
        elif data[first] < data[second]:
            winner = second
        else:
            winner = "Ничья"
        await message.answer(f"Сравнение:\n{first} ({data[first]}) vs {second} ({data[second]})\n🏆 Победитель: {winner}")
        pets_selected = []

# Планировщик для обновления значений каждые 12 часов
scheduler = BackgroundScheduler()
scheduler.add_job(update_values, "interval", hours=12)
scheduler.start()

# Запуск бота
if __name__ == "__main__":
    update_values()  # обновляем данные при старте
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)