import requests
ERROR = {"EMPTY_STATE": "Строка пуста"}
DIVIDER = "="*25

while(True):
    text =  input("Client: ")
    if (text == ""):
        text = ERROR["EMPTY_STATE"]
    api_url = 'http://localhost:5000/'
    r = requests.get(url=api_url+text)
    print("Server: " + r.text)
    print(DIVIDER)
