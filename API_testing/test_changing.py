import requests
import pytest
import random
import json

auth = "Bearer 0fe3aeb1c4cc0554f01883ad3a131472ebac81d02ece138df93390ef8cbba804"
header = {
    "Authorization" : auth
}
base_url = "https://gorest.co.in/"
endpoints = "public/v2/users"
url = base_url+endpoints
random_num = random.randint(1000,9999)

@pytest.fixture()
def user_id():
    random_num = random.randint(1000,9999)
    data = {
     "name": "Mukund_velraj",
     "email": f"mukundvelraj{random_num}@mail.com",
     "gender": "male",
     "status": "active"
    }
    response = requests.post(url,json=data,headers=header)
    assert response.status_code == 201,f"The Bad request {response.status_code}"
    user_no = response.json()["id"]
    print(user_no)
    return user_no
    assert response.json()["name"] == "Mukund"
    assert response.json()["status"] == "active"

def test_put(user_id):
    put_url = f"{url}/{user_id}"
    data = {
     "name": "Mukund Velraj",
     "email": f"mukundvelraj{random_num}@mail.com",
     "gender": "male",
     "status": "inactive"
    }
    response = requests.put(put_url,json=data,headers=header)
    json_data = response.json()
    print(f"Put Response : {json.dumps(json_data,indent=5)}")
    assert response.status_code == 200, f"bad Rq {response.status_code}"
    assert json_data["status"] == "inactive"

def test_patch(user_id):
    patch_url = f"{url}/{user_id}"
    data = {
        "name" : "Vanitha",
        "gender":"female",
        "email" : f"vanitha{random_num}@gmail.com",
        "status": "active"
    }
    response = requests.patch(patch_url,json=data,headers= header)
    json_data = response.json()
    print(f"The Updated data : {json.dumps(json_data,indent=5)}")
    assert response.status_code == 200
    assert json_data["gender"] == "female"
    assert json_data["name"] == "Vanitha"
