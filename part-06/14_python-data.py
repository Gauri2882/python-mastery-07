""" Understanding web scraping basics """
""" Adding dynamic updates for real time tracking """

import requests
from bs4 import BeautifulSoup
import time


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None
    
def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://www.google.com/finance/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    
    soup = parse_html(html)
    price_tag = soup.find("div", class_="rPF6Lc")
    name = soup.find("div", class_ = "zzDege")
    if price_tag:
        return price_tag.text, name.text
    else:
        print("Stock price not found")
        return None
    
def track_stock_price(ticker, interval =  60):
    while True:
        price, name = get_stock_price(ticker)
        if price:
            print(f"{ticker} : {price}")
        time.sleep(interval) 
    
ticker = "AAPL:NASDAQ"

price, name = get_stock_price(ticker)
if price:
    print(f"The current price of {ticker} ({name}) is {price}")

track_stock_price(ticker, 2)


