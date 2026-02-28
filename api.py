import requests

API_KEY = "YOUR_API_KEY"
SITE_KEY = "0x4AAAAAAAaa"
SITE_URL = "https://example.com/"

url = "https://wssolver.net/solve"

params = {
    "apikey": API_KEY,
    "sitekey": SITE_KEY,
    "siteurl": SITE_URL
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print("Response:", response.text)
