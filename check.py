import os
import replicate
api_token = os.environ.get("REPLICATE_API_TOKEN")

client = replicate.Client(api_token=api_token)

try:
    models = client.models.list()
    print("API token is valid. Successfully retrieved models.")
except replicate.exceptions.ReplicateError as e:
    print(f"API token is invalid or there's an error: {e}")