import requests
import json

base_url = "https://gorest.co.in/"
endpoints = "public/v2/users/8010486"
url = base_url+endpoints
response = requests.get(url)
assert response.status_code == 200,f"Error - {response.status_code}"
result = json.dumps(response.json(),indent=5)
print(result)


header = {
    "Authorization" : "Bearer 1d4f6a63667a0e76ef5ab92a738f59d338d49fecba05471e35546f54465d0b2e"
}

data = {
    "status": "inactive"
}

response_patch = requests.patch(url,json=data,headers=header)
assert response_patch.status_code == 200, f"Wrong code received {response.status_code}"
result1 = json.dumps(response_patch.json(),indent=5)
print(result1) 


