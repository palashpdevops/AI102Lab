# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import requests

# Configuration - replace these with your actual values
language_key = "62uJDIOhXHgi6xtzyfR9tSWIKmhmCUCFSkj7344dzHbLoOIach4rJQQJ99BEACYeBjFXJ3w3AAAAACOGkxC6"
language_endpoint = "https://pphub2997981559.cognitiveservices.azure.com/"
blob_url = "https://zasedemo102.blob.core.windows.net/ai102demo/AIDemo.txt"  # Public blob URL

def authenticate_text_client():
    """Authenticate the Text Analytics client"""
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=language_endpoint,
        credential=ta_credential)
    return text_analytics_client

def read_text_from_public_blob():
    """Read text content from a publicly accessible blob URL"""
    try:
        response = requests.get(blob_url)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.text
    except Exception as e:
        print(f"Error fetching from blob URL: {e}")
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

def sample_extractive_summarization(client):
    """Perform extractive summarization on text from a public blob"""
    from azure.ai.textanalytics import ExtractiveSummaryAction

    # Read text from public blob URL
    input_text = read_text_from_public_blob()

    if input_text:
        print("\nAnalyzing text from input.txt...")
        language_detection_example(client, input_text)

    if not input_text:
        print("No text was retrieved from blob URL.")
        return

    # Prepare document for analysis (must be a list)
    document = [input_text]

    # Start the analysis
    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    # Get results
    document_results = poller.result()
    
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("\nSummary extracted:")
            print(" ".join([sentence.text for sentence in extract_summary_result.sentences]))

# Authenticate and run the summarization
text_client = authenticate_text_client()
sample_extractive_summarization(text_client)
