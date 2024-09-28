import requests
import json
from datetime import datetime

# Facebook credentials and IDs
ACCESS_TOKEN = 'EAAHM8w5HhegBO3AjsxJbda0oZAyTzqz4aB76cVrZALoTnij4Y2mtGQKYfZAJBPcZBbg4GyDafa3acFWuZBRiXjDI4tWDKAYTS3wwJrL8alktn5hj82FcbTTFhXJuoAeHJk1lS1k7ewPhrj17ZAX4V70WEjOpTtFqJoSALByv0t7PjB1aTKhHLNtnPOdFJuUbgZD'
PAGE_ID = '113877840441644'  # iCodeguru page ID
KEYWORDS = ["Crash Course"]
START_DATE = "2024-03-03T00:00:00"
END_DATE = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# Function to check if the post contains any of the keywords (case-insensitive)
def contains_keyword(post_text, keywords):
    if not post_text:
        return False
    for keyword in keywords:
        if keyword.lower() in post_text.lower():
            return True
    return False

# Facebook Graph API request to get posts with video links
def get_video_posts_with_keywords(page_id, access_token, start_date, end_date, keywords):
    url = f"https://graph.facebook.com/v15.0/{page_id}/posts"
    
    params = {
        'fields': 'message,created_time,attachments{media_type,url},permalink_url',
        'access_token': access_token,
        'since': start_date,
        'until': end_date,
    }
    
    all_matching_posts = []
    
    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break
        
        data = response.json()
        
        for post in data.get('data', []):
            # Check if the post contains video media
            attachments = post.get('attachments', {}).get('data', [])
            for attachment in attachments:
                if attachment.get('media_type') == 'video':
                    message = post.get('message', '')
                    created_time = post.get('created_time', '')
                    post_url = post.get('permalink_url', '')
                    
                    # Check if the post contains any of the specified keywords
                    if contains_keyword(message, keywords):
                        all_matching_posts.append({
                            'url': post_url,
                            'created_time': created_time,
                            'message': message
                        })
        
        # Check if there is a next page
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
        else:
            break
    
    return all_matching_posts

# Get matching posts
matching_posts = get_video_posts_with_keywords(PAGE_ID, ACCESS_TOKEN, START_DATE, END_DATE, KEYWORDS)

# Print the results
if matching_posts:
    print(f"Found {len(matching_posts)} matching posts with videos:")
    for post in matching_posts:
        print(f"Post URL: {post['url']}")
        print(f"Created Time: {post['created_time']}")
        print(f"Message: {post['message']}")
        print("-" * 40)
else:
    print("No matching video posts found.")
