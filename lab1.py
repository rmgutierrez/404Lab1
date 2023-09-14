import requests

print(requests.__version__)

resp = requests.get('https://raw.githubusercontent.com/rmgutierrez/404Lab1/main/lab1.py')

print(resp.text)