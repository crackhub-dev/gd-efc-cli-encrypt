import requests
import json
import sys
import re
#decryption server in base64
decrypt_server = "ZGVjcnlwdC5jcmFja2h1YjIxMzE5OTEud29ya2Vycy5kZXY="
#no trailing slash at the end below
instance = "https://drive.crackhub.site"
link = sys.argv[1]
find_id = re.findall("[-\w]{25,}", link)
folder_id = find_id[0]
data = '{"folder":"' + folder_id +'"}'
response = requests.post(f'{instance}/encrypt', data=data)
if response.json()["status"] == "ok":
    enc_id = response.json()["data"]
    print(f"{instance}/#{decrypt_server}.{enc_id}")
else:
    print("error, check input")
