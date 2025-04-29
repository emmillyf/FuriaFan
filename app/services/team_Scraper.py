from parsel import Selector
from requests.exceptions import RequestException
import cloudscraper

def get_furia_info():

    try:
        scraper = cloudscraper.create_scraper()
        r = scraper.get('https://www.hltv.org/team/8297/furia')
        selector = Selector(text=r.text)
        
        ranking_valve = selector.xpath('//div[@class="profile-team-stat"]//span[@class="right"]/a[contains(@href, "teamId=8297")]/text()').get()
        world_ranking = selector.xpath('//div[@class="profile-team-stat"]//span[@class="right"]/a[contains(@href, "/ranking/teams")]/text()').get()
        weeks_top30 = selector.xpath('//div[contains(@class, "profile-team-stat") and contains(.//b, "Weeks in top30")]/span[@class="right"]/text()').get()
        average_age = selector.xpath('//div[contains(@class, "profile-team-stat") and contains(.//b, "Average player age")]/span[@class="right"]/text()').get()

        return {
                "ranking_valve": ranking_valve,
                "world_ranking": world_ranking,
                "weeks_top30": weeks_top30,
                "average_age": average_age
                }
    
    except RequestException as e:
        if r.status_code != 200:
            return print("Erro na requisição")

