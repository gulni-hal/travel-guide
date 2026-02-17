import requests
from bs4 import BeautifulSoup
import re

def clean_text(text):
    # Gereksiz ifadeleri temizle
    text = re.sub(r"TIKLAYIN.*", "", text)
    text = re.sub(r"İncelemek için.*", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def scrape_roma():
    url = "https://www.bizevdeyokuz.com/roma"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    content = soup.find("div", class_="entry-content")

    texts = []

    if content:
        for tag in content.find_all(["h2", "h3", "p"]):  # li kaldırdık
            text = tag.get_text(strip=True)
            if text:
                cleaned = clean_text(text)
                if len(cleaned) > 40:  # çok kısa spam cümleleri alma
                    texts.append(cleaned)

    return "\n\n".join(texts)
