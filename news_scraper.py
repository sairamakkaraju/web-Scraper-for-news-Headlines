import requests
from bs4 import BeautifulSoup

# URL of a news website (example: BBC)
url = "https://www.bbc.com/news"

# Fetch the webpage
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find headlines - most news sites use <h2> or <h3> for headlines
headlines = soup.find_all(['h2', 'h3'])

# Extract text and clean it
clean_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

# Save headlines to a .txt file
with open("news_headlines.txt", "w", encoding="utf-8") as file:
    for idx, title in enumerate(clean_headlines, start=1):
        file.write(f"{idx}. {title}\n")

print("✅ Headlines successfully saved to 'news_headlines.txt'")
