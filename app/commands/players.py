import discord
from discord import app_commands

@app_commands.command(name="jogadores", description="Mostra os jogadores do time FURIA")
async def jogadores(interaction: discord.Interaction):
    await interaction.response.defer()
    
    embed = discord.Embed(
        title="FURIA | Jogadores",
        description="Lista com os nomes dos jogadores do time de CS:GO da FURIA e suas funções durante o game",
        color=0xFFFFFF
    )
    embed.add_field(name="FalleN", value=" 🎯 AWPer / 👑 IGL", inline=False)
    embed.add_field(name="yuurih", value="🔫 Rifler / 🕵️ Lurker", inline=False)
    embed.add_field(name="YEKINDAR", value="💥Entry Fragger", inline=False)
    embed.add_field(name="KSCERATO", value="🔫 Cerato - Rifle /  🏠 Closer", inline=False)
    embed.add_field(name="molody", value=" 🛡️ Suporte / 🎭 Flex", inline=False)
    embed.add_field(name="Chelo", value="🔫 Rifler | Reserva", inline=False)
    embed.add_field(name="skullz", value="🔫 Rifler | Reserva", inline=False)

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")

    await interaction.followup.send(embed=embed)
