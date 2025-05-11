
# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="OpenAI-endpoint-url",
    api_key="5zXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE",  # Directly put the API key here
)

result = client.images.generate(
    model="dall-e-3",  # the name of your DALL-E 3 deployment
    prompt="A football match moment",
    n=1  # You had 'undefined' here, which is invalid. Setting it to 1.
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print("Generated Image URL:", image_url)
