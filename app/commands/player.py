import discord
from discord import app_commands
from services.player_Scraper import get_player_info
from services.player_Stats_Scraper import get_player_stats

@app_commands.command(name="jogador", description="Informações e estatísticas de um jogador")
async def jogador(interaction: discord.Interaction, nome: str):
    await interaction.response.defer()
    
    FURIA_PLAYERS = {
        "fallen": 2023, "Gabriel Toledo": 2023, "Fallen": 2023, 
        "kscerato": 15631, "Kaike Cerato": 15631, "kaike": 15631,
        "YEKINDAR": 13915, "Mareks Gaļinskis": 13915,
        "yuurih": 12553, "Yuri Santos": 12553, "yuri": 12553,
        "skullz": 18676, "Felipe Medeiros": 18676,
        "chelo": 10566, "Marcelo Cespedes": 10566, "Cespedes": 10566, 
        "molody": 24144, "Danil Golubenko": 24144
    }
    
    if nome.lower() not in FURIA_PLAYERS:
        valid_players = "\n".join(f"- {name.capitalize()}" for name in FURIA_PLAYERS.keys())
        embed = discord.Embed(
            title="Jogador não encontrado",
            description=f"Jogadores disponíveis:\n{valid_players}",
            color=0xFFFFFF
        )
        return await interaction.followup.send(embed=embed)

    data = get_player_info(nome)
    if not data:
        return await interaction.followup.send("Erro ao buscar dados do jogador")

    embed = discord.Embed(
        description=f"*{data.get('real_name', 'N/A')}*",
        color=0xFFFFFF
    )

    embed.set_author(
        name=f"{data.get('nick_name')}",
        icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/730/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
    )

    if data.get('image'):
        embed.set_image(url=data['image'])  
    
    embed.add_field(name="🕒 Idade", value=data.get('age', 'N/A'), inline=True)
    embed.add_field(name="👥 Time Atual", value=data.get('current_team', 'N/A'), inline=False)
    embed.add_field(name="💰 Prêmio em dinheiro", value=data.get('prize_money', 'N/A'), inline=True)


    data_stats = get_player_stats(nome)

    stats = data_stats.get('stats', {})
    
    stats_value = (
        f"**Rating:** {stats.get('rating_1', 'N/A')}\n"
        f"**HS%:** {stats.get('headshot_percentage', 'N/A')}\n"
        f"**KPR:** {stats.get('kills_per_round', 'N/A')}\n"
        f"**DPR:** {stats.get('damage_per_round', 'N/A')}\n"
        f"**K/D Ratio:** {stats.get('kd_ratio', 'N/A')}\n"
        f"**Total Kills:** {stats.get('total_kills', 'N/A')}\n"
        f"**Total Deaths:** {stats.get('total_deaths', 'N/A')}\n"
        f"**Mapas Jogados:** {stats.get('maps_played', 'N/A')}\n"


    )

    embed.add_field(name="📊 Estatísticas", value=stats_value, inline=False)
    
    embed.set_footer(text="Fonte: HLTV.org")
    await interaction.followup.send(embed=embed)