import requests
import random
res = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')

print(res.json())