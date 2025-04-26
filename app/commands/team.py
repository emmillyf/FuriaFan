import discord
from discord import app_commands
from utils.team_Scraper import get_furia_info

@app_commands.command(name="time", description="Informações sobre o time")
async def time(interaction: discord.Interaction):
    await interaction.response.defer() 

    data = get_furia_info()
    
    embed = discord.Embed(
        title="FURIA | Time",
        description="**Treinador:** Sid Macedo",
        color=0xFFFFFF
    )
    embed.add_field(name="🔧 Ranking Valve", value=data.get('ranking_valve', 'N/A'), inline=False)
    embed.add_field(name="🌍 Ranking Mundial", value=f"{data.get('ranking_valve', 'N/A')} 🏆", inline=False)
    embed.add_field(name="📅 Semanas no top 30", value=f"{data.get('world_ranking', 'N/A')} 🏅", inline=False)
    embed.add_field(name="👥 Média da idade dos jogadores", value=data.get('average_age', 'N/A'), inline=False)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
    embed.set_footer(text="Fonte: HLTV.org")

    await interaction.followup.send(embed=embed)
