# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import requests

# Configuration - replace these with your actual values
language_key = "Replace-my-language-key"
language_endpoint = "https://pphubxxxxx.cognitiveservices.azure.com/"
blob_url = "https://zasdemo1.blob.core.windows.net/textstote/AISummary.txt"  # Public blob URL

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

def sample_extractive_summarization(client):
    """Perform extractive summarization on text from a public blob"""
    from azure.ai.textanalytics import ExtractiveSummaryAction

    # Read text from public blob URL
    input_text = read_text_from_public_blob()

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
