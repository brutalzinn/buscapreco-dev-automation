import requests

def loginAuth():
    r = requests.post("http://127.0.0.1:8000/v1/user/auth",json={'email':'admin@example.com','senha':'123'})
    print(r.status_code, r.reason)
    json_response = r.json()
    if r.status_code != 200:
        return False
    return json_response['data']['token']