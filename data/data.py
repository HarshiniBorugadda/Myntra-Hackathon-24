import pandas as pd
from instagram_api import get_instagram_data
from tiktok_api import get_tiktok_data
from pinterest_api import get_pinterest_data
from amazon_api import get_amazon_data
from web_scraper import scrape_ajio, scrape_myntra

# Collect data
instagram_data = get_instagram_data()
tiktok_data = get_tiktok_data()
pinterest_data = get_pinterest_data()
amazon_data = get_amazon_data()
ajio_data = scrape_ajio()
myntra_data = scrape_myntra()

# Create DataFrames
df_instagram = pd.DataFrame(instagram_data)
df_tiktok = pd.DataFrame(tiktok_data)
df_pinterest = pd.DataFrame(pinterest_data)
df_amazon = pd.DataFrame(amazon_data)
df_ajio = pd.DataFrame(ajio_data)
df_myntra = pd.DataFrame(myntra_data)

# Data cleaning and transformation
def clean_and_transform(df):
    df['date'] = pd.to_datetime(df['date'])
    df['engagement'] = df['likes'] + df['comments'] + df['shares']
    return df

dfs = [df_instagram, df_tiktok, df_pinterest, df_amazon, df_ajio, df_myntra]
cleaned_dfs = [clean_and_transform(df) for df in dfs]

# Integrate data
integrated_df = pd.concat(cleaned_dfs, ignore_index=True)

# Map to common schema
integrated_df = integrated_df.rename(columns={
    'product_name': 'item_name',
    'product_price': 'price',
    'product_category': 'category'
})

# Save integrated data
integrated_df.to_csv('integrated_fashion_data.csv', index=False)
