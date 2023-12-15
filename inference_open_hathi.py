import requests
import os
from dotenv import load_dotenv

load_dotenv()

hugging_face_key = os.getenv("HUGGING_FACE_KEY")

API_URL = "https://api-inference.huggingface.co/models/sarvamai/OpenHathi-7B-Hi-v0.1-Base"
headers = {"Authorization": f"Bearer {hugging_face_key}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)
