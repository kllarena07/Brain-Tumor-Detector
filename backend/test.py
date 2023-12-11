import requests

resp = requests.post("http://127.0.0.1:8080/predict", files={'file': open('8no.jpg', 'rb')})

print(resp.text)