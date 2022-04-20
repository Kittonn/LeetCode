import requests
import random
res = requests.get('https://cheab-quote.herokuapp.com')

num = len(res.json()['quote'])
n = random.randint(0,num)
print(res.json()['quote'][n])
