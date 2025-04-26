import discord
from discord import app_commands

@app_commands.command(name="jogadores", description="Mostra os jogadores do time FURIA")
async def jogadores(interaction: discord.Interaction):
    await interaction.response.defer()
    
    embed = discord.Embed(
        description="Lista com os nomes dos jogadores do time de CS:GO da FURIA e suas funções durante o game",
        color=0xFFFFFF
    )
    
    embed.set_author(
        name="FURIA | Jogadores",
        icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/730/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
    )

    embed.add_field(name="FalleN", value=" 🎯 AWPer / 👑 IGL", inline=False)
    embed.add_field(name="yuurih", value="🔫 Rifler / 🕵️ Lurker", inline=False)
    embed.add_field(name="YEKINDAR", value="💥Entry Fragger", inline=False)
    embed.add_field(name="KSCERATO", value="🔫 Cerato - Rifle /  🏠 Closer", inline=False)
    embed.add_field(name="molody", value=" 🛡️ Suporte / 🎭 Flex", inline=False)
    embed.add_field(name="skullz", value="🔫 Rifler | 🕵️ Lurker", inline=False)
    embed.add_field(name="Chelo", value=" 💺 Banco de Reserva", inline=False)

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")

    await interaction.followup.send(embed=embed)
