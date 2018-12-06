import string
import random
import requests

url = "https://testloginspam.weebly.com/ajax/apps/formSubmitAjax.php"

with open("names.txt", "r") as r:
    names = r.read().split("\n")
    r.close()

for name in names:
    email = name + random.choice(string.digits) + random.choice(string.digits) + "@gmail.com"
    start = ''.join(random.choice(string.ascii_uppercase))
    password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    password2 = ''.join(random.choice(string.digits) for i in range(4))
    password = start + password1 + password2

    postdata = {
        '_u542666988292124176': email,
        '_u771030282848478735': password
    }

    requests.post(url, allow_redirects=False, data=postdata)

    print(f"Sending Email: {email} Password: {password}")
