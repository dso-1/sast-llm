from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["NVIDIA_API_KEY"],
    base_url="https://integrate.api.nvidia.com/v1"
)

models = client.models.list()

for model in models.data:
    print(model.id)