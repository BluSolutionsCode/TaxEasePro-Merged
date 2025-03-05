import os
from convert_pdf_script import convert_pdf
from extract_text_script import extract_text

# Define input folder for PDFs
INPUT_FOLDER = "uploads"

def process_all_pdfs():
    """Processes all PDFs: Converts them to images and extracts text"""
    
    # Ensure the uploads folder exists
    if not os.path.exists(INPUT_FOLDER):
        print(f"❌ Error: Folder '{INPUT_FOLDER}' not found.")
        return

    # Process all PDF files in the uploads directory
    for pdf_file in os.listdir(INPUT_FOLDER):
        if pdf_file.endswith(".pdf"):
            print(f"🔄 Processing: {pdf_file}")
            
            image_paths = convert_pdf(pdf_file)
            
            if image_paths:
                for image in image_paths:
                    extract_text(image)

    print("✅ Auto processing pipeline complete!")

if __name__ == "__main__":
    process_all_pdfs()

