import requests
import re
import json
pattern = "[(.*?)]"

search_list = ["https://www.microcenter.com/product/621439/raspberry-pi-4-model-b-2gb-ddr4"]

def get_stock(page):
  for item in response.text.split("\n"):
    if "var inventory" in item:
      #result = re.search('\[(.*)\]', item.strip())
      result = item.split("= ",1)[1].strip()
      stock = json.loads(result)
      for location in stock:
          if location.get('qoh') > 0: 
            print("%d at %s" % (location.get('qoh'), location.get('storeName')))
      #print(json.dumps(stock, sort_keys=True, indent=4))
      #print(result)

for item in search_list:  
  response = requests.get(item)
  page = response.text
  get_stock(page)
