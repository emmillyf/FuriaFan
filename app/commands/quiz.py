import discord
from discord import app_commands
from services.quiz_Services import gerar_pergunta
import asyncio

player_scores = {}

@app_commands.command(name="quiz", description="Quiz sobre o time da FURIA")
async def quiz(interaction: discord.Interaction):
    await interaction.response.defer()

    player_name = str(interaction.user)
    if player_name not in player_scores:
        player_scores[player_name] = 0
    
    embed = discord.Embed(
        title="FURIA | Quiz",
        description="Responda as perguntas sobre o time FURIA de CSGO!\n"
        "Digite **parar** a qualquer momento para encerrar.\n\n",
        color=0xFFFFFF
    )

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
    await interaction.followup.send(embed=embed)
    
    pontuacao = 0
    total_perguntas = 1
    
    while True:
        try:
            dados_pergunta = gerar_pergunta() 
            pergunta = dados_pergunta["pergunta"]
            alternativas = dados_pergunta["alternativas"]
            resposta_correta = dados_pergunta["resposta_correta"]
            total_perguntas += 1

            embed = discord.Embed(
                description=f"**{pergunta}**",
                color=0xFFFFFF
            )
            embed.set_author(
                name=f"FURIA | Round: {total_perguntas-1}",
                icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/730/69f7ebe2735c366c65c0b33dae00e12dc40edbe4.jpg",
            )
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
            embed.set_footer(text="Responda com A, B, C, D ou 'parar'")
            
            opcoes_texto = "\n".join([f"**{letra}**) {texto}" for letra, texto in alternativas.items()])
            embed.add_field(
                name="Opções:",
                value=opcoes_texto,
                inline=False
            )

            await interaction.followup.send(embed=embed)

            def check(m):
                return (
                    m.channel == interaction.channel and
                    m.author == interaction.user and
                    m.content.lower() in ['a', 'b', 'c', 'd', 'parar']
                )

            try:
                msg = await interaction.client.wait_for('message', check=check, timeout=30.0)
                
                if msg.content.lower() == 'parar':
                    player_scores[player_name] += pontuacao
                    
                    
                    end_embed = discord.Embed(
                        title="🏁 Quiz Encerrado",
                        description=f"**Pontuação final:** {pontuacao} pontos\n"
                                f"Obrigado por jogar!",
                        color=0x00FF00
                    )

                    await interaction.followup.send(embed=end_embed)
                    return
                    
                if msg.content.upper() == resposta_correta:
                    pontuacao += 1
                    player_scores[player_name] += 1
                    
                    correct_embed = discord.Embed(
                        description=f"⭐ {interaction.user.mention} acertou!!!\n",
                        color=0x00FF00
                    )

                    correct_embed.set_author(
                        name="CORRETO!!"
                    )

                    await interaction.followup.send(embed=correct_embed)
                else:
                    wrong_embed = discord.Embed(
                        title="❌ Resposta Incorreta",
                        description=f"A resposta correta era: **{resposta_correta}**",
                        color=0xFF0000
                    )
                    await interaction.followup.send(embed=wrong_embed)
                    
                await asyncio.sleep(1)  
                    
            except asyncio.TimeoutError:
                timeout_embed = discord.Embed(
                    description=f"⏳ Tempo esgotado! A resposta era: **{resposta_correta}**\n"
                            f"Próxima pergunta...",
                    color=0xFFFFFF
                )
                await interaction.followup.send(embed=timeout_embed)
                await asyncio.sleep(1)
                
        except Exception as e:
            error_embed = discord.Embed(
                title="❌ Ocorreu um erro",
                description=f"Erro ao gerar pergunta: {str(e)}",
                color=0xFF0000
            )
            await interaction.followup.send(embed=error_embed)
            return