import discord
from discord import app_commands
from app.utils.team_Stats_Scraper import get_team_stats

@app_commands.command(name="estatisticas", description="Estatísticas do time")
async def estatisticas(interaction: discord.Interaction):
    await interaction.response.defer() 

    data = get_team_stats()
    if not data:
        return await interaction.followup.send("Erro ao buscar estatísticas do time")
    
    embed = discord.Embed(
        title="FURIA | Estatísticas do Time",
        description="📊",
        color=0xFFFFFF
    )
    embed.add_field(name=" Mapas Jogados", value=data.get('maps_played', 'N/A'), inline=False)
    embed.add_field(name=" Rounds Jogados", value=data.get('rounds_played', 'N/A'), inline=False)
    embed.add_field(name=" Vitórias / Empates / Derrotas", value=data.get('WDL', 'N/A'), inline=False)
    embed.add_field(name=" KD/D Ratio", value=data.get('kd_ratio', 'N/A'), inline=False)
    embed.add_field(name=" Total de kills", value=data.get('total_kills', 'N/A'), inline=False)
    embed.add_field(name=" Total de mortes", value=data.get('total_deaths', 'N/A'), inline=False)

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
    embed.set_footer(text="Fonte: HLTV.org")

    await interaction.followup.send(embed=embed)
