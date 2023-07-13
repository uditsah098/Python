import requests

req=requests.get("https://www.ansible.com/")
if req.status_code==200:
    print("sucess")
else:
    print(req.status_code)   