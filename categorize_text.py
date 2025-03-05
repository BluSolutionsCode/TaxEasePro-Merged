import openai
import json
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Function to categorize text using OpenAI GPT-4
def categorize_text(text):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that categorizes financial documents into predefined categories."},
                {"role": "user", "content": f"Categorize this document text: {text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ Error categorizing text: {e}")
        return None

# Read extracted text and categorize
input_dir = "extracted_text"
output_file = "extracted_text/categorized_text.json"
categorized_data = {}

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_dir, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            print(f"🔍 Categorizing {filename}...")
            category = categorize_text(text)
            if category:
                categorized_data[filename] = category

# Save results
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(categorized_data, json_file, indent=4)

print(f"✅ Categorization completed! Results saved at: {output_file}")

