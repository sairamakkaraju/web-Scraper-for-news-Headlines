# web-Scraper-for-news-Headlines
Scrape top news headlines from a news website and save them to a .txt file.

🛠️ Tools Used
Python
requests (to fetch HTML)
BeautifulSoup from bs4 (to parse HTML)

Deliverables
news_scraper.py → the Python script
news_headlines.txt → the text file containing scraped headlines

How It Works
The script sends an HTTP request to fetch the HTML content of a news website.
BeautifulSoup parses the page and extracts all <h2> or <h3> tags (commonly used for headlines).
The extracted headlines are cleaned and written to a .txt file.
