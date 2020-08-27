import requests
import json

response=requests.get("https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=csv&offset=0&limit=1000")
data=response.content.decode('utf-8')
print(data)