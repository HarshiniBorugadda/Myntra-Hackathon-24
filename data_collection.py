import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape data from a website (e.g., a fashion blog)
def scrape_blog_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example scraping
    posts = soup.find_all('article')
    data = []
    for post in posts:
        title = post.find('h2').text
        date = post.find('time')['datetime']
        content = post.find('div', class_='entry-content').text
        data.append({'Title': title, 'Date': date, 'Content': content})
    
    return pd.DataFrame(data)

# Example usage
url = 'https://example-fashion-blog.com'
data = scrape_blog_data(url)
data.to_csv('blog_data.csv', index=False)
