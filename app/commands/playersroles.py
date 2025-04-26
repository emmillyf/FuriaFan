import discord
from discord import app_commands

@app_commands.command(name="rotas", description="Informações sobre as rotas dos jogadores em game")
async def rotas(interaction: discord.Interaction):
    await interaction.response.defer()
    
    embed = discord.Embed(
        title="FURIA | Rotas",
        description="Explicação detalhada de cada função dos jogadores durante o game",
        color=0xFFFFFF
    )
    embed.add_field(name="🎯 AWPer", value="Especialista no uso da sniper (AWP)", inline=False)
    embed.add_field(name=" 👑 IGL", value="In-Game Leader(IGL), líder tático que toma as decisões estratégicas durante a partida", inline=False)
    embed.add_field(name="🔫 Rifler", value="Especialista no uso de rifles (AK-47, M4A4, M4A1-S)", inline=False)
    embed.add_field(name="🕵️ Lurker", value="Jogador que atua de forma independente para cortar rotas inimigas", inline=False)
    embed.add_field(name="💥Entry Fragger", value="Responsável por abrir espaços no bomb site inimigo (muitas vezes o primeiro a morrer)", inline=False)
    embed.add_field(name="🏠 Closer", value="Jogador que atua em combates corpo a corpo (curta distância)", inline=False)
    embed.add_field(name="🛡️ Suporte", value="Focado em utilidades (smokes, flashes) e assistência ao time", inline=False)
    embed.add_field(name="🎭 Flex", value="Jogador versátil que adapta-se a múltiplas funções conforme necessário", inline=False)

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")

    await interaction.followup.send(embed=embed)