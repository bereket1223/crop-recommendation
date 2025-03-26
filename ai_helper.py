import openai  # For ChatGPT
import requests  # For DeepSeek

# Use OpenAI API
openai.api_key = "your_openai_api_key"

def get_crop_tips(crop_name):
    prompt = f"Give me best farming tips for growing {crop_name} efficiently."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
