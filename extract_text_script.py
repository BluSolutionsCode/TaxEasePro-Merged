from google.cloud import vision
import os
import json

# Google Vision API Client
client = vision.ImageAnnotatorClient()

# Input and output folders
image_folder = "processed"
text_output_folder = "extracted_text"

# Ensure output directory exists
os.makedirs(text_output_folder, exist_ok=True)

def extract_text(image_path):
    """Extracts text from an image using Google Vision API"""
    with open(image_path, "rb") as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        extracted_text = texts[0].description
    else:
        extracted_text = "No text detected."

    return extracted_text

# Process all images in the processed folder
extracted_data = {}

for image_file in os.listdir(image_folder):
    if image_file.endswith(".jpg"):
        image_path = os.path.join(image_folder, image_file)
        extracted_text = extract_text(image_path)

        text_file_path = os.path.join(text_output_folder, f"{image_file}.txt")
        with open(text_file_path, "w") as text_file:
            text_file.write(extracted_text)
        
        extracted_data[image_file] = extracted_text
        print(f"✅ Extracted text saved: {text_file_path}")

# Save all extracted text as JSON
json_output_path = os.path.join(text_output_folder, "extracted_text.json")
with open(json_output_path, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"✅ Text extraction completed! JSON saved at: {json_output_path}")

