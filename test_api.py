import openai
import sys
sys.path.append('reverie/backend_server')
from utils import openai_api_key

openai.api_key = openai_api_key

try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Say hello",
        max_tokens=5
    )
    print(response.choices[0].text)
except Exception as e:
    print(f"Error: {e}")
