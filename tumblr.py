import pytumblr
import json
from pprint import pprint
from slugify import slugify

# Authenticate via API Key
client = pytumblr.TumblrRestClient('kKxQPoWzMVDCRIUcseJwm1NuVFYxEOIeDn2B0E0tmtrVrpkyju')

# Make the request
post_data = []
for i in range(0,11): #218 total posts on tumblr
  #  Tumblr requests are capped at 20 so I needed to offset by 20 more each iteration
  arr = client.posts('nvraghuram.tumblr.com', offset=20*i)['posts']
  for p in arr:
    post_data.append(p)

#dump into tumblr.json file --> huge takes forever to open
with open('tumblr.json', 'w') as f:
  json.dump(post_data, f)

posts = []
count = 1
data = post_data

# Parse posts array & create json array formatted properly for ghost
# will paste into json file and import into ghost later
for p in data:
  title = p["title"] if 'title' in p else p["short_url"]
  body = p["body"] if 'body' in p else p["short_url"]
  post = {
    "id": count,
    "title": title,
    "slug": slugify(title),
    "markdown": body,
    "html": body,
    "status": "published",
    "language": "en_US",
    "meta_title": title,
    "author_id": 1,
    "created_at": p["date"],
    "created_by": 1,
    "updated_at": p["date"],
    "updated_by": 1,
    "published_at": p["date"],
    "published_by": 1
  }
  count += 1
  posts.append(post)

# Write post array to file
with open('data.json', 'w') as f:
  json.dump(posts, f)
