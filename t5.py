import pandas as pd
from instascrape import Hashtag

# Function to scrape and save data
def scrape_and_save_data(hashtag_url, output_csv, cookies):
    # Create Hashtag instance
    fashion_hashtag = Hashtag(hashtag_url)

    # Assign cookies to the Hashtag instance
    fashion_hashtag.cookies = cookies

    try:
        # Scrape data
        fashion_hashtag.scrape()

        # Extract recent posts
        posts_data = []
        for post in fashion_hashtag.get_recent_posts():
            post_data = {
                'Post URL': post.url,
                'Caption': post.caption,
                'Likes': post.likes,
                'Comments': post.comments,
                'Timestamp': post.timestamp,
                'Hashtags': post.hashtags,
                'Location': post.location_name if post.location_name else 'Not specified',
            }
            posts_data.append(post_data)

        # Convert to DataFrame
        df = pd.DataFrame(posts_data)

        # Save to CSV
        df.to_csv(output_csv, index=False)
        print(f"Data saved to {output_csv}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    hashtag_url = "https://www.instagram.com/explore/tags/fashion/?hl=en"
    output_csv = "fashion_trends_data.csv"
    cookies = {
        "sessionid": "------------------------------",
        # Add other necessary cookies if required
    }
    scrape_and_save_data(hashtag_url, output_csv, cookies)
