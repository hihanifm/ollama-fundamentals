import requests
import os

# Use system certificates instead of certifi bundle
system_cert_path = "/etc/ssl/cert.pem"
if os.path.exists(system_cert_path):
    os.environ['REQUESTS_CA_BUNDLE'] = system_cert_path
    os.environ['CURL_CA_BUNDLE'] = system_cert_path

url = "http://192.168.1.214:34005"
full_url = url + "/api/generate"
data = {"prompt": "hello"}
response = requests.api.post(full_url, json=data)
if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

# print(response.utils.get_auth_from_url(full_url))
print(f"Using certificate bundle: {os.environ.get('REQUESTS_CA_BUNDLE', requests.certs.where())}")