import discord
import settings

cfg = settings.Config()
client = discord.Client()

@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.startwith("inicio"):
            await msg.channel.send('respuesta')

client.run(cfg.TOKEN)