import discord
from discord import app_commands

@app_commands.command(name="inventario", description="Acesso ao inventário de algum jogador")
async def inventario(interaction: discord.Interaction, jogador: str):
    """Comando para mostrar o inventário de CS:GO de um jogador da FURIA"""
    await interaction.response.defer()
    
    PLAYERS_STEAM = {
        "fallen": {
            "url": "https://steamcommunity.com/id/fallencs/inventory/#730",
            "nick": "FalleN",
            "real_name": "Gabriel Toledo"
        },
        "kscerato": {
            "url": "https://steamcommunity.com/id/kscthebesten/inventory/#730",
            "nick": "KSCERATO",
            "real_name": "Kaike Cerato"
        },
        "YEKINDAR": {
            "url":"https://steamcommunity.com/id/yrgod/inventory/#730",
            "nick": "YEKINDAR"
        },
        "yuurih": {
            "url":  "https://steamcommunity.com/id/ahsislife/inventory/#730",
            "nick": "yuurih"
        },
        "skullz": {
            "url": "https://steamcommunity.com/id/skullzcsgo/inventory/#730", 
            "nick": "skullz"
        },
        "chelo" : {
            "url": "https://steamcommunity.com/id/chelovqv/inventory/#730",
            "nick": "chelo"
        },
        "molody": {
            "url":	"https://steamcommunity.com/id/smknevida/inventory/#730",
            "nick": "molody" 
        }   
    }

    
    if jogador.lower() not in PLAYERS_STEAM:
        valid_players = "\n".join(f"- {data['nick']}" for data in PLAYERS_STEAM.values())
        embed = discord.Embed(
            title="Jogador não encontrado",
            description=f"Jogadores disponíveis:\n{valid_players}",
            color=0xFFFFFF
        )
        return await interaction.followup.send(embed=embed)
    
    data = PLAYERS_STEAM[jogador]

    embed = discord.Embed(color=0xFFFFFF)
    
    embed.set_author(
        name=data.get('nick'),
        icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/730/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
        url=data.get('url')
    )
    
    embed.add_field(
        name="🔗 Inventário CS:GO",
        value=f"[Acessar na Steam]({data.get('url')})",
        inline=False
    )
    
    await interaction.followup.send(embed=embed)