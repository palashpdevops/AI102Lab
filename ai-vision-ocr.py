import requests
from PIL import Image
import io
import os
import time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Azure Computer Vision Configuration
subscription_key = "5vCQ9WNkHfbQ7hX5yCtlhgAM8pt9q3EYw8cXnbdXHxB8PYBPFhg4JQQJ99BDACYeBjFXJ3w3AAAFACOGlYNk"  # or replace with your key
endpoint = "https://palashaidemo.cognitiveservices.azure.com/"

def read_text_from_image(image_url):
    try:
        # Initialize Azure Computer Vision client
        computervision_client = ComputerVisionClient(
            endpoint,
            CognitiveServicesCredentials(subscription_key))

        # Call Azure OCR API
        ocr_result = computervision_client.read(image_url, raw=True)

        # Get the operation location (async operation)
        operation_location = ocr_result.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]

        # Wait for the async operation to complete
        while True:
            result = computervision_client.get_read_result(operation_id)
            if result.status.lower() not in ['notstarted', 'running']:
                break
            time.sleep(1)

        # Extract and return the text
        text = ""
        if result.status.lower() == 'succeeded':
            for page in result.analyze_result.read_results:
                for line in page.lines:
                    text += line.text + "\n"
        return text.strip()

    except Exception as e:
        print(f"Error processing image with Azure Computer Vision: {e}")
        return None

# Example usage
if __name__ == "__main__":
    image_url = "https://palashocr.blob.core.windows.net/ocrdemo/ai-image.jpg"  # Replace with your image URL

    # Set your Azure credentials (or use environment variables)
    os.environ["AZURE_COMPUTER_VISION_KEY"] = "5vCQ9WNkHfbQ7hX5yCtlhgAM8pt9q3EYw8cXnbdXHxB8PYBPFhg4JQQJ99BDACYeBjFXJ3w3AAAFACOGlYNk"
    os.environ["AZURE_COMPUTER_VISION_ENDPOINT"] = "https://palashaidemo.cognitiveservices.azure.com/"

    extracted_text = read_text_from_image(image_url)
    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Failed to extract text")
