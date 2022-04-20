import requests
import random
<<<<<<< HEAD
res = requests.get('https://cheab-quote.herokuapp.com')

num = len(res.json()['quote'])
n = random.randint(0,num)
print(res.json()['quote'][n])
=======
res = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')

print(res.json())
>>>>>>> parent of b2f1341 (update date in command gatpat and saman)
