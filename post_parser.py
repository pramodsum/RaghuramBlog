import json
from pprint import pprint
from slugify import slugify

with open('tumblr.json') as data_file:
    data = json.load(data_file)

post_data = data['posts']
posts = []
count = 1

for p in post_data:
  title = p["title"] if 'title' in p else p["caption"]
  body = p["body"] if 'body' in p else p["permalink_url"]
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

with open('data.json', 'w') as f:
  json.dump(posts, f)
