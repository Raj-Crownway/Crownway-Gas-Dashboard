import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def fetch_gas_prices(zip_code="63123"):
    url = f"https://www.gasbuddy.com/home?search={zip_code}&fuel=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    stations = []
    results = soup.find_all("div", class_="GenericStationListItem__stationListItem")

    for item in results:
        try:
            name = item.find("h3").text.strip()
            address = item.find("div", class_="GenericStationListItem__stationAddress").text.strip()
            price = item.find("span", class_="StationDisplayPrice__price").text.strip().replace("$", "")
            stations.append({
                "Station": name,
                "Address": address,
                "Regular": f"${price}",
                "Last Updated": datetime.now().strftime("%I:%M %p")
            })
        except Exception:
            continue

    df = pd.DataFrame(stations)
    df.to_csv("gas_data.csv", index=False)

if __name__ == "__main__":
    fetch_gas_prices()
