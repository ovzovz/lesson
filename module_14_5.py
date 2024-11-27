from aiogram.dispatcher.filters.state import State, StatesGroup, default_state
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from api import  api
from crud_functions import *

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
button4 = KeyboardButton(text='Регистрация')
kb.add(button1, button2, button3, button4)

prod_kb=InlineKeyboardMarkup()
prod_button=[]
products = get_all_products()
for product in products:
    prod_button.append(InlineKeyboardButton(f'{product[1]}',
                        callback_data='product_buying'))
prod_kb.add(*prod_button)

in_kb=InlineKeyboardMarkup()
in_button1 = InlineKeyboardButton('Рассчитать норму калорий',
                               callback_data='calories')
in_button2 = InlineKeyboardButton('Формулы расчёта',
                                  callback_data='formulas')
in_kb.add(in_button1, in_button2)

class RegistrationState (StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await sing_up(message)

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'],data['email'],data['age'])
    await message.answer('Регистрация завершена')
    await state.finish()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def starter(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)

@dp.callback_query_handler(text='formulas')
async  def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; \n" +
         " для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',
                         reply_markup=kb)

@dp.message_handler(state=UserState.age)
async def set_growth(message,state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
        await state.update_data(weight=message.text)
        data = await state.get_data()
        res = 10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])-161
        await message.answer(f'Ваша норма калорий (жен.): {res}')
        await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        text_answer= (f'Название: {product[1]} | Описание:  {product[2]} | Цена: {product[3]}')
        with open(f'prod_14_4/{product[1]}.jpg', 'rb') as img:
            await message.answer_photo(img, text_answer)
    await message.answer('Выберите продукт для покупки:', reply_markup=prod_kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
