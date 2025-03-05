from pdf2image import convert_from_path
import os

# Define input and output directories
input_folder = "uploads"
output_folder = "processed"

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# List all PDF files in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

if not pdf_files:
    print("❌ No PDF files found in the uploads folder.")
    exit()

# Convert each PDF to images
for pdf_file in pdf_files:
    pdf_path = os.path.join(input_folder, pdf_file)
    
    try:
        images = convert_from_path(pdf_path)
        
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"{pdf_file}_page_{i+1}.jpg")
            image.save(image_path, "JPEG")
            print(f"✅ Saved: {image_path}")

    except Exception as e:
        print(f"❌ Error processing {pdf_file}: {e}")

print("✅ PDF conversion completed!")

