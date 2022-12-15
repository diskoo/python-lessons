from aiogram import Bot, Dispatcher, executor, types

import python_weather

# bot init
bot = Bot(token='5882517471:AAGHtBd-534qB7f3e1LdN7aXng1rsicQMhA')
dp = Dispatcher(bot)
# чета тута не работает походу
client = python_weather.Client(format=python_weather.IMPERIAL)
    
# echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)

    celsius = round((weather.current.temperature-32)*0.55)

    resp_msg = weather.location_name + '\n'
    resp_msg += f'Текущая температура: {celsius}°\n'
    resp_msg += f'Состояние погоды: {weather.current.sky_text}'

    if celsius <= 10:
        resp_msg += '\n\n Прохладно! Одевайтесь потеплее!'
    else:
        resp_msg += '\n\n Тепло! Одевайтесь полегче!'

    await message.answer(resp_msg)

# run long-polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)