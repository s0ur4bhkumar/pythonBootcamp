from datetime import datetime

import requests

USERNAME = "apt3x"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "kjdsh234khjhdfwoi23423405sdfg"
today = datetime.now()
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {"X-USER-TOKEN": TOKEN}

# respone = requests.post(url=pixela_endpoint, json=user_params)
# print(respone.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Meditation",
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai",
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"
# pixel_config = {"date": today.strftime('%y%m%d'), "quantity": "10"}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/20260505"
# update_config = {
#     'quantity':'7'
# }

# response = requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)

delete_endpoint = f"{update_endpoint}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
