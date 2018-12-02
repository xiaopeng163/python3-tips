import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)