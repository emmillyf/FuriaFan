import discord
from discord import app_commands

@app_commands.command(name="redesocial", description="Redes sociais da FURIA")
async def redesocial(interaction: discord.Interaction):
    await interaction.response.defer() 

    redesSociais = {
        "📸 Instagram": "https://www.instagram.com/furiagg",
        "🛒 Loja": "https://www.furia.gg/",
        "𝕏 Twitter/X": "https://x.com/FURIA",
        "🎥 YouTube": "https://www.youtube.com/furiagg",
        "🎮 Twitch": "https://www.twitch.tv/furiagg",
        "💬 Discord": "https://discord.gg/furia"

    }

    embed = discord.Embed(
        color=0xFFFFFF
    )

    embed.set_author(
        name="FURIA | Redes Sociais"
    )

    for nome, link in redesSociais.items():
        embed.add_field(
            name=nome,
            value=f"[Clique aqui]({link})",
            inline=False
        )

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
    embed.set_footer(text="Siga a FURIA nas redes sociais!")

    await interaction.followup.send(embed=embed)
