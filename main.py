import discord

from bot_logic import flip_coin
from bot_logic import gen_emodji
from bot_logic import gen_pass
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()
    if message.content.startswith('Привет') or message.content.startswith('привет') or message.content.startswith('пр') or message.content.startswith('Пр') or message.content.startswith('Ку') or message.content.startswith('ку'):
        await message.channel.send("Дарова!")
    elif message.content.startswith('Пока') or message.content.startswith('пока') or message.content.startswith('пок') or message.content.startswith('Пок') or message.content.startswith('покеда') or message.content.startswith('Покеда'):
        await message.channel.send("Наконецто ты уходишь")
    elif message.content.startswith('Я не с тобой разговариваю!') or message.content.startswith('Я не с тобой разговариваю') or message.content.startswith('я не с тобой разговариваю') or message.content.startswith('я не с тобой разговариваю!'):
        await message.channel.send("А с кем?У тебя же нет друзей")
    elif message.content.startswith('Че сказал?') or message.content.startswith('че сказал?') or message.content.startswith('че сказал') or message.content.startswith('Че сказал'):
        await message.channel.send("Че слышал")
    elif message.content.startswith('Обидно было') or message.content.startswith('обидно было') or message.content.startswith('обидно было') or message.content.startswith('Вообщето обидно было') or message.content.startswith('вообщето обидно было'):
        await message.channel.send("Ладно прости(UwU)")
    elif message.content.startswith('Создай мне рандомный пароль') or message.content.startswith('создай мне рандомный пароль'):
        await message.channel.send(f'{gen_pass(10)}')
    elif message.content.startswith('Монетку') or message.content.startswith('монетку'):
        await message.channel.send(f'{flip_coin(10)}')
    elif message.content.startswith('дай мне рандомный эмодзи') or message.content.startswith('Дай мне рандомный эмодзи'):
        await message.channel.send(f'{gen_emodji(10)}')
#    else:
#        await message.channel.send(message.content)
async def on_message_delete(self, message):
    msg = f'{message.author} has deleted the message: {message.content}'
    await message.channel.send(msg)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("token")
