import requests
import json

# Load credentials
with open('settings.json', 'r') as file:
    settings = json.load(file)

TOKEN = settings.get('telegram_bot_token')
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url)

# Ensure the response is properly printed
print(response.text.encode('utf-8').decode('utf-8'))
