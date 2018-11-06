# To try my hand at webscraping
# https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
# article is potentially oudated, but I'll just implement first
# I will probably try https://www.datacamp.com/community/tutorials/web-scraping-using-python next

# import libraries
import urllib3
import urllib
from bs4 import BeautifulSoup

quote_page = "https://www.bloomberg.com/quote/SPX:IND"
#http = urllib3.PoolManager()
#response = http.request('GET',quote_page)
#soup = BeautifulSoup(response.data.decode('utf-8'),'html.parser')
#name_box = soup.find('span', attrs={'class': lambda L: L and L.startswith('priceText')})

html = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(html, 'html.parser')
#name_box = soup.find('span', attrs={'class': 'priceText__1853e8a5'})
name_box = soup.find('title')
name = name_box.text.strip()
print(name)
