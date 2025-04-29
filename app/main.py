from discord import app_commands
from dotenv import load_dotenv
from commands import time, jogadores, rotas, jogador, estatisticas, inventario, replay, quiz, redesocial
import discord
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("Token do bot não encontrado! Verifique seu arquivo .env")

class FuriaFanBot(discord.Client):

    # configuração de inicialização do bot
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="$",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.add_command(time)
        self.tree.add_command(jogadores)
        self.tree.add_command(jogador)
        self.tree.add_command(rotas)
        self.tree.add_command(estatisticas)
        self.tree.add_command(inventario)
        self.tree.add_command(replay)
        self.tree.add_command(quiz)
        self.tree.add_command(redesocial)
        await self.tree.sync()

    async def on_ready(self):
        print(f'Bot conectado como {self.user}')

bot = FuriaFanBot()
bot.run(TOKEN)