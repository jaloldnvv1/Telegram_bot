import asyncio
import logging
import sys
import json
from config import TOKEN
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(F.text.isdigit())
async def get_user_data(message: Message):
    with open("users.json", "r") as file:
        users = json.load(file)
    await message.answer(json.dumps(users[message.text]))


@dp.message()
async def salom(message: Message) -> None:
    try:
        if "salom" in message.text.lower():
            await message.answer("Va aleykum assalom")
        else:
            await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
