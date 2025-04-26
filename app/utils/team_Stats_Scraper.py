from parsel import Selector
from requests.exceptions import RequestException
import cloudscraper


def get_team_stats():

    try:
        scraper = cloudscraper.create_scraper()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        url = f"https://www.hltv.org/stats/teams/8297/furia"
        r = scraper.get(url, headers=headers)
        r.raise_for_status()
        selector = Selector(text=r.text)

        def extract_text(xpath):
            result = selector.xpath(xpath).get()
            print(f"DEBUG: {xpath} => {result}")
            return selector.xpath(xpath).get(default='N/A').strip()

        return {
                "maps_played": extract_text('//div[@class= "columns"][1]//div[@class="col standard-box big-padding"][1]//div[@class="large-strong"][1]/text()'),
                "WDL":  extract_text('//div[@class= "columns"][1]//div[@class="col standard-box big-padding"][2]//div[@class="large-strong"][1]/text()'),
                "total_kills": extract_text('//div[@class= "columns"][1]//div[@class="col standard-box big-padding"][3]//div[@class="large-strong"][1]/text()'),
                "total_deaths": extract_text('//div[@class= "columns"][2]//div[@class="col standard-box big-padding"][1]//div[@class="large-strong"][1]/text()'),       
                "rounds_played": extract_text('//div[@class= "columns"][2]//div[@class="col standard-box big-padding"][2]//div[@class="large-strong"][1]/text()'),
                "kd_ratio":extract_text('//div[@class= "columns"][2]//div[@class="col standard-box big-padding"][3]//div[@class="large-strong"][1]/text()')
        }

    except RequestException as e:
        print(f"Request failed: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None