import instaloader
import boto3

# Initialize Instaloader
loader = instaloader.Instaloader()

# Fetch posts for a hashtag or profile
hashtag = "fashion"
posts = instaloader.Hashtag.from_name(loader.context, hashtag).get_posts()

# Initialize S3 client
s3 = boto3.client('s3',
                  aws_access_key_id='YOUR_ACCESS_KEY',
                  aws_secret_access_key='YOUR_SECRET_KEY')

# Example bucket and key (replace with your own)
bucket_name = 'your-bucket-name'
file_key = 'fashion_data.json'

# Write data to a JSON file
data = []
for post in posts:
    post_data = {
        'Post URL': f"https://www.instagram.com/p/{post.shortcode}/",
        'Caption': post.caption,
        'Likes': post.likes,
        'Comments': post.comments,
        'Timestamp': post.date_utc.timestamp(),
        'Hashtags': post.caption_hashtags,
        'Location': post.location,
    }
    data.append(post_data)

# Upload data to S3
s3.put_object(Bucket=bucket_name, Key=file_key, Body=json.dumps(data))

print(f"Data uploaded to S3 bucket: {bucket_name}/{file_key}")
