# import cloudscraper
# from parsel import Selector

# def get_furia_ranking():
#     scraper = cloudscraper.create_scraper()
#     r = scraper.get('https://www.hltv.org/team/8297/furia')
    
#     if r.status_code != 200:
#         print(f"Erro ao acessar a página. Status code: {r.status_code}")
#         return None

#     selector = Selector(text=r.text)  
#     world_ranking = selector.xpath('//div[@class="profile-team-stat"]//span[@class="right"]/a[contains(@href, "/ranking/teams")]/text()').get()
        
#     print(f"world_ranking: {world_ranking}")

#     if world_ranking:
#         world_ranking = world_ranking.strip() 
#         print(f"O ranking atual da FURIA é: {world_ranking}")
#         return world_ranking
#     else:
#         print("Ranking não encontrado.")
#         return None

# get_furia_ranking()


#####################################

# import discord
# from discord import app_commands
# from utils.furiaTeamScraper import get_furia_info

# @app_commands.command(name="team", description="Mostra informações sobre o time FURIA")
# async def team(interaction: discord.Interaction):
#     await interaction.response.defer()  # caso demore um pouco

#     data = get_furia_info()
    
#     embed = discord.Embed(
#         title="Time FURIA — Informações",
#         description=(
#         f"**Valve Ranking:** {data.get['ranking']}\n"
#         f"**World Ranking:** {data.get['world_ranking']}"
#     ),
#         color=0x000000
#     )
#     embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/pt/f/f9/Furia_Esports_logo.png")
#     embed.set_footer(text="Fonte: HLTV.org")

#     await interaction.followup.send(embed=embed)
import cloudscraper
from parsel import Selector

def get_furia_stats():
    scraper = cloudscraper.create_scraper()
    url = "https://www.hltv.org/stats/teams/8297/furia"
    
    try:
        # Faz a requisição com cloudscraper
        r = scraper.get(url)
        r.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        selector = Selector(text=r.text)
        
#         # XPath ajustado para weeks in top30
#         weeks_top30 = selector.xpath('//div[contains(@class, "profile-team-stat") and contains(.//b, "Weeks in top30")]/span[@class="right"]/text()').get()
        maps_played = selector.xpath('//div[@class="col standard-box big-padding"][1]//div[@class="large-strong"][1]/text()').get()
        print(maps_played) 
#         # XPath ajustado para average age
#         coach = selector.xpath('//div[.//b[contains(., "Coach")]]/a/text()[normalize-space()]').get()

        
#         print(f"Weeks in top30: {weeks_top30}")
#         print(f"coach: {coach}")
        
        # return {
        #     "weeks_top30": weeks_top30,
        #     "average_age": average_age
        # }
        
    except Exception as e:
        print(f"Erro ao acessar HLTV: {e}")
        return None

# Executa a função
stats = get_furia_stats()
