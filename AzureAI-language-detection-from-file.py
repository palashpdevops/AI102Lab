
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

======================================================================
# This program takes input from a file input.txt where the text notes in any language may be saved. The program will analyse the language
############################################################################################################################################
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Get Azure Language Service credentials from environment variables


def authenticate_client():
    """Authenticate the client using your key and endpoint"""
    ta_credential = AzureKeyCredential("My-Azure_Key")
    text_analytics_client = TextAnalyticsClient(
        endpoint="cognitiveservices.azure.endpoint",
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
###################################################
# Another version - It will ask input file name from user
##################################################

import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Get Azure Language Service credentials from environment variables
#language_key = os.environ.get('LANGUAGE_KEY')  # Update with your environment variable name
#language_endpoint = os.environ.get('LANGUAGE_ENDPOINT')  # Update with your environment variable name

def authenticate_client():
    """Authenticate the client using your key and endpoint"""
    ta_credential = AzureKeyCredential("egAQuq3uPZxl6QXjYtXWcZk6fvIwfeSCyUXz30960Wg7uz8QTiQaJQQJ99BEACYeBjFXJ3w3AAAAACOGAv6E")
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
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def detect_language(client, text):
    """Detect the language of the provided text"""
    if not text:
        print("No text provided for language detection.")
        return None

    try:
        # Azure Text Analytics supports up to 10 documents per request
        documents = [text]
        response = client.detect_language(documents=documents, country_hint='us')[0]
        return response.primary_language
    except Exception as err:
        print(f"Encountered exception during language detection: {err}")
        return None

def main():
    # Get input filename from user
    file_path = input("Enter the path to the text file you want to analyze: ").strip()
    
    if not file_path:
        print("No file path provided. Exiting.")
        return
    
    # Read the file content
    text_content = read_text_from_file(file_path)
    if text_content is None:
        return
    
    # Initialize Azure client
    client = authenticate_client()
    
    # Detect language
    detected_language = detect_language(client, text_content)
    
    if detected_language:
        print("\nLanguage Detection Results:")
        print(f"File: {file_path}")
        print(f"Detected Language: {detected_language.name}")
        print(f"Confidence Score: {detected_language.confidence_score:.2%}")
    else:
        print("Language detection failed.")

if __name__ == "__main__":
    main()
    
