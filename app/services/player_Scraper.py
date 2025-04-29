from parsel import Selector
from requests.exceptions import RequestException
import cloudscraper

FURIA_PLAYERS = {
        "fallen": 2023, "Gabriel Toledo": 2023, "Fallen": 2023, 
        "kscerato": 15631, "Kaike Cerato": 15631, "kaike": 15631,
        "YEKINDAR": 13915, "Mareks Gaļinskis": 13915,
        "yuurih": 12553, "Yuri Santos": 12553, "yuri": 12553,
        "skullz": 18676, "Felipe Medeiros": 18676,
        "chelo": 10566, "Marcelo Cespedes": 10566, "Cespedes": 10566, 
        "molody": 24144, "Danil Golubenko": 24144
}

def get_player_info(player_name: str):
    """Extrai dados do jogador específico do HLTV"""
    player_id = FURIA_PLAYERS.get(player_name.lower())
    if not player_id:
        return None

    try:
        scraper = cloudscraper.create_scraper()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        url = f"https://www.hltv.org/player/{player_id}/player"
        r = scraper.get(url, headers=headers)
        r.raise_for_status()
        selector = Selector(text=r.text)

        def extract_text(xpath):
            result = selector.xpath(xpath).get()
            return selector.xpath(xpath).get(default='N/A').strip()

        return {
            "nick_name": extract_text('//h1[@class="playerNickname"]/text()'),
            "real_name": extract_text('//div[@class="playerRealname"]/text()'),
            "age": extract_text('//div[@class="playerInfoRow playerAge"]//span[@itemprop="text"]/text()'),
            "prize_money": extract_text('//div[@class="playerInfoRow playerPrizeMoney"]/span[@class="listRight"]/text()'),
            "current_team": extract_text('//div[contains(@class, "playerTeam")]//a[contains(@href, "/team/8297/furia")]/text()'),
            "image": selector.xpath('//img[@class="bodyshot-img"]/@src').get()
        }

    except RequestException as e:
        print(f"Request failed: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None