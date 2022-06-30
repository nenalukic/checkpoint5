import requests

def get_phone(name):
    if name == "Urban":
        phone = requests.get('http://localhost:5000/api?action=phone&name=Urban')
        return phone.text   
    else:
        return "Unknown name"
    
def get_name(phone):
    if phone == "0435-4355438":
        name = requests.get("http://localhost:5000/api?action=name&phone=0435-4355438")
        return name.text
    else:
        return "Unknown phone number"
    