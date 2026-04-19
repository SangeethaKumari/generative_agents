import requests
import json

API_BASE = "http://10.0.10.51:8123/v1"
API_KEY = "sv-openai-api-key"

print(f"Querying models from {API_BASE}/models...")
try:
    response = requests.get(
        f"{API_BASE}/models",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    if response.status_code == 200:
        models = response.json()
        print(json.dumps(models, indent=2))
        
        # Filter for models that might be embeddings
        print("\nPossible embedding models found:")
        found = False
        for model in models.get('data', []):
            model_id = model.get('id', '')
            if 'embed' in model_id.lower() or 'bert' in model_id.lower() or 'ada' in model_id.lower():
                print(f"- {model_id}")
                found = True
        if not found:
            print("No obvious embedding models found in the list.")
    else:
        print(f"Failed with status code: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"Error querying server: {e}")
