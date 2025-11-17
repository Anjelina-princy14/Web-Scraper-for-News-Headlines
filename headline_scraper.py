import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.bbc.com/news"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        print("❌ Error fetching the page:", e)
        return

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")

    # Extract unique headlines
    headlines = []
    seen = set()
    for tag in h2_tags:
        text = tag.get_text(strip=True)
        if text and text not in seen:
            seen.add(text)
            headlines.append(text)

    # Save ONLY headlines to the .txt file (meets PDF requirement)
    output_file = "headlines.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")

    # ❤️ Impressive Terminal Output (not saved in file)
    print("\n" + "=" * 50)
    print(" 📰 NEWS HEADLINE SCRAPER - SUCCESS 🎉")
    print("=" * 50)
    print(f"📌 Total UNIQUE headlines scraped: {len(headlines)}")
    print(f"📁 Saved to: {output_file}")
    print("=" * 50)
    print("\n✨ Sample Headlines:\n")
    for h in headlines[:5]:
        print(f" ➤ {h}")

if __name__ == "__main__":
    scrape_headlines()
