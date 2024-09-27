from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def scrape_fasion_page():
  async with async_playwright() as pw:
    browser = await pw.chromium.launch(headless=False)
    page = await browser.new_page()
    
    await page.goto("https://www.instagram.com/explore/tags/fashion/")
    await page.wait_for_timeout(5000)

    imgs = await page.query_selector_all("img")
    data = []
    for img in imgs:
      src = await img.get_attribute("src")
      alt = await img.get_attribute("alt")
      if alt and alt.startswith("Photo"):
        data.append([src, alt])
    df = pd.DataFrame(data, columns=["src", "alt"])
    df.to_csv("data.csv")

if __name__ == "__main__":
  asyncio.run(scrape_fasion_page())
