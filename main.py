import requests
import re
pattern = "[(.*?)]"

response = requests.get('https://www.microcenter.com/product/621439/raspberry-pi-4-model-b-2gb-ddr4')
#print(response.text)
for item in response.text.split("\n"):
  if "var inventory" in item:
    result = re.search('\[(.*)\]', item.strip())
    print(result.group(1))
