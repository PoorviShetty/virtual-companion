API_TOKEN = open("./notebooks/hf_token.txt","r").read()
import requests

API_URL = "https://api-inference.huggingface.co/models/philschmid/bart-large-cnn-samsum"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def summarise_text(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]['summary_text']
