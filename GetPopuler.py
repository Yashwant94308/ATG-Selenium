import requests, json

response = requests.get(
    'https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=22a1377a56b4c384b61b723a80a73492'
    '&user_id=193065083%40N04&format=json&nojsoncallback=1')
print(response.json())
