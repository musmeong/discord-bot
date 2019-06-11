from random import randint
from imgurpython import ImgurClient

client_id = '463e415e4ff7895'
client_secret = '314f276c187ac67b5c58b9d6dfbaaa763f0008ca'

client = ImgurClient(client_id, client_secret)

# Example request
items = client.subreddit_gallery('indonesia', sort='time', window='week', page=randint(0,4))
print(items[randint(0,99)].title)
