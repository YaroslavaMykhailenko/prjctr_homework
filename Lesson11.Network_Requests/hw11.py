import requests
user_input = input('Enter a word you want to search in Giphy site:')
key = 'XbeZdOLHJYimhuTk6CU9MdYCB21V69EL'
giphy_resp = requests.get(
    'http://api.giphy.com/v1/gifs/search?',
    params={
        'api_key': key,
        'q': f'{user_input}',
        'limit' : '10'
    }
)

for obj in giphy_resp.json():
    print(f'object: {giphy_resp.json()[obj]}')