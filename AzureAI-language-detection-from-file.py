
# This program takes input from a file input.txt where the text notes in any language may be saved. The program will analyse the language
############################################################################################################################################
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Get Azure Language Service credentials from environment variables


def authenticate_client():
    """Authenticate the client using your key and endpoint"""
    ta_credential = AzureKeyCredential("egAQuXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXACOGAv6E")
    text_analytics_client = TextAnalyticsClient(
        endpoint="https://hub11623521841.cognitiveservices.azure.com/",
        credential=ta_credential
    )
    return text_analytics_client

def read_text_from_file(file_path):
    """Read text content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def language_detection_example(client, text):
    """Detect the language of the provided text"""
    if not text:
        print("No text provided for language detection.")
        return

    try:
        # Split text into chunks if needed (Azure has length limits)
        documents = [text]
        response = client.detect_language(documents=documents, country_hint='us')[0]
        print(f"Detected Language: {response.primary_language.name}")
        print(f"Confidence Score: {response.primary_language.confidence_score:.2f}")
    except Exception as err:
        print(f"Encountered exception: {err}")

def main():
    client = authenticate_client()
    
    # Read text from input file
    input_text = read_text_from_file('input.txt')
    
    if input_text:
        print("\nAnalyzing text from input.txt...")
        language_detection_example(client, input_text)

if __name__ == "__main__":
    main()
(myvenv) root@souvikvm04may:~/application# 
