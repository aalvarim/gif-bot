import os
import discord

TOKEN = "MTM0NTA0MzI3OTcyNDU0ODE0Ng.GNoULM.iNaUYLfzSHFKmTYPPJwCnlzySOy2zpr-68VJeM"  # Pegando token da variável de ambiente

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Necessário para ler mensagens

client = discord.Client(intents=intents)

# Dicionário de usuários e seus GIFs
user_gifs = {
    464832828102672394: "https://media.discordapp.net/attachments/1041429282611802143/1041782896693874749/bloggif_62b85b1b34b59.gif",  # dark
    620629615144206346: "https://tenor.com/view/ichigo-kurosaki-ichigo-kurosaki-kurosaki-ichigo-from-the-back-gif",  # zé
}

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Evita que o bot responda a si mesmo

    gif = user_gifs.get(message.author.id)  # Pega o GIF do usuário
    if gif:
        await message.channel.send(gif)  # Envia o GIF específico

client.run(TOKEN)
