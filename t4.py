from instascrape import Hashtag, Profile
import requests
import json
import csv
# Your cookies from the browser
cookies = {
    "sessionid": "67635442072%3AyY31HnkqY2FKGG%3A16%3AAYeVTzdoDpztuPd_1lK29ljYEpsPClo8jGp_thhk-g",
    # Include other relevant cookies if needed
}

# Create a Hashtag instance
fash = Hashtag("https://www.instagram.com/explore/tags/fashion/?hl=en")

# Assign cookies to the Hashtag instance
fash.cookies = cookies

# Scrape data
fash.scrape()

# Print the scraped data
data = fash.json_dict
csv_file = "fashion_data.csv"
with open(csv_file, mode = 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(data.keys())
    writer.writerow(data.values())