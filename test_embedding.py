import openai
import os

# Set the same config as in the app
API_BASE = "http://10.0.10.51:8123/v1"
API_KEY = "sv-openai-api-key"

openai.api_key = API_KEY
openai.api_base = API_BASE

print(f"Testing embedding request to {API_BASE}...")
try:
    response = openai.Embedding.create(
        input=["hello world"],
        model="text-embedding-ada-002"
    )
    print("Success!")
    print(response)
except Exception as e:
    print(f"Failed with error: {e}")
    # Try to see if we can get more info by using requests directly
    import requests
    try:
        r = requests.post(
            f"{API_BASE}/embeddings",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"input": ["hello world"], "model": "text-embedding-ada-002"}
        )
        print(f"Direct request status code: {r.status_code}")
        print(f"Direct request response text: {r.text}")
    except Exception as e2:
        print(f"Direct request also failed: {e2}")
