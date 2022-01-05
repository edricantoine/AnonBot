import requests
import main
import discord
import random

res = requests.get("https://oauth.reddit.com/r/greentext/new",
                   headers=main.headers)


client = discord.Client()

GUILD = 'Bot test'


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    msg = message.content
    if 'What would Anon do?' in msg or 'what would anon do?' in msg or 'what would Anon do?' in msg or 'What would anon do?' in msg:
        rand = random.randint(0, 24)
        pst = res.json()['data']['children'][rand]
        await message.channel.send(pst['data']['title'])


client.run('token')
