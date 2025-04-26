import discord
from discord import app_commands

@app_commands.command(name="replay", description="Replay das melhores jogadas")
async def replay(interaction: discord.Interaction):
    await interaction.response.defer()

    REPLAYS = {
        "🏆 IEM Rio Major 2022": "https://www.youtube.com/watch?v=XGsWbUJy9Fk",
        "🔫 Melhores momentos do FalleN": "https://www.youtube.com/watch?v=zGIgj3wO6Nw",
        "💥 Destaques do KSCERATO": "https://www.youtube.com/watch?v=hygqehEXukw",
        "🎯 Melhores jogadas do yuurih": "https://www.youtube.com/watch?v=Nkq4Q3X0gy0",
        "🔥 Highlight reel do YEKINDAR": "https://www.youtube.com/watch?v=pNAoLWvJXbs"
    }

    embed = discord.Embed(
        color=0xFFFFFF,
    )
        
    embed.set_author(
        name="Melhores replays da FURIA",
        icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/730/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
    )

    for name, url in REPLAYS.items():
        embed.add_field(
            name=name,
            value=f"[Assistir]({url})",
            inline=False
        )

    await interaction.followup.send(embed=embed)