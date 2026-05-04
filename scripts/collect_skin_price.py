import csv
import os
from datetime import datetime
from urllib.parse import quote
import requests


def replacing_formats(price):
    price = float(price.replace("R$ ", "").replace(",", "."))
    return price


skins = [
    "AK-47 | Redline (Field-Tested)",
    "AWP | Asiimov (Field-Tested)",
    "M4A4 | Desolate Space (Field-Tested)"
]


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(project_root, "data", "raw", "skins_data.csv")
file_exists = os.path.exists(csv_path)


with open(csv_path, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "skin_name",
            "lowest_price",
            "median_price",
            "volume",
            "collected_at"
        ])

    for skin in skins:
        print(f"Collecting: {skin}")

        encoded_skin = quote(skin)
        url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=7&market_hash_name={encoded_skin}"

        response = requests.get(url)
        data = response.json()

        if not data.get("success"):
            print(f"Error collecting data for: {skin}")
            continue

        lowest = replacing_formats(data["lowest_price"])
        median = replacing_formats(data["median_price"])
        volume = int(data["volume"])
        collected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([skin, lowest, median, volume, collected_at])