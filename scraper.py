import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    # answer kisminda cikan ifadeleri sub ile temizledik
    text = re.sub(r"TIKLAYIN.*", "", text)
    text = re.sub(r"İncelemek için.*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def scrape_roma():
    url = "https://www.bizevdeyokuz.com/roma"
    # kullandigim websitesi
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", class_="entry-content")

    texts = []

    if content:
        for tag in content.find_all(["h2", "h3", "p"]):  
            # linkleri kaldirmak icin asko
            text = tag.get_text(strip=True)
            if text:
                cleaned = clean_text(text)
                if len(cleaned) > 40:  
                    # cok kisa spam cumleleri alma
                    texts.append(cleaned)

    return "\n\n".join(texts)
