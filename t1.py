import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Function to get fashion news from NewsAPI
def get_fashion_news():
    api_key = "-----------------"  # Replace with your actual NewsAPI key
    url = f"https://newsapi.org/v2/everything?q=fashion+trends&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()['articles']
    return pd.DataFrame(articles)

# Function to create a requests session with retries
def create_session():
    session = requests.Session()
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

# Function to scrape basic product data from a hypothetical e-commerce site
def scrape_ecommerce_data(url, session):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        for product in soup.find_all('div', class_='product'):
            name = product.find('h2').text.strip()
            price = product.find('span', class_='price').text.strip()
            category = product.find('span', class_='category').text.strip()
            products.append({'name': name, 'price': price, 'category': category})
        return pd.DataFrame(products)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()

# Create a session with retry mechanism
session = create_session()

# Collect data
print("Collecting fashion news data...")
df_news = get_fashion_news()

print("Collecting e-commerce data...")
# Replace these URLs with actual e-commerce sites you have permission to scrape
df_ecommerce1 = scrape_ecommerce_data("https://example-fashion-store1.com", session)
time.sleep(2)  # Be polite, wait between requests
df_ecommerce2 = scrape_ecommerce_data("https://example-fashion-store2.com", session)

# Data cleaning and transformation
def clean_and_transform(df, source):
    if source == 'news':
        df['date'] = pd.to_datetime(df['publishedAt'])
        df['engagement'] = df['title'].str.len() + df['description'].str.len()  # Simple engagement metric
    elif source == 'ecommerce':
        df['date'] = pd.to_datetime('today')
        df['engagement'] = 1  # Placeholder
    return df

print("Cleaning and transforming data...")
df_news = clean_and_transform(df_news, 'news')
df_ecommerce1 = clean_and_transform(df_ecommerce1, 'ecommerce')
df_ecommerce2 = clean_and_transform(df_ecommerce2, 'ecommerce')

# Integrate data
print("Integrating data...")
dfs = [df_news, df_ecommerce1, df_ecommerce2]
integrated_df = pd.concat(dfs, ignore_index=True)

# Map to common schema
integrated_df = integrated_df.rename(columns={
    'title': 'item_name',
    'name': 'item_name',
    'price': 'price',
    'category': 'category'
})

# Save integrated data
print("Saving integrated data...")
integrated_df.to_csv('integrated_fashion_data.csv', index=False)

print("Data integration complete. Results saved to 'integrated_fashion_data.csv'")
