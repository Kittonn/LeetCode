import requests

res = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
print(res.json()[0]['txn_date'])