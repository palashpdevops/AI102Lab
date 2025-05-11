(myvenv) root@ppaidemo:~/application# cat appsummary.py 

# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
#language_key = os.environ.get('LANGUAGE_KEY')
#language_endpoint = os.environ.get('LANGUAGE_ENDPOINT')

language_key = "8PDzkOEyo3J9ICANsOJ2HCiomdDYaWmVtoAxSPX9WRo74mKM9vxiJQQJ99BEACYeBjFXJ3w3AAAAACOGREc9"
language_endpoint = "https://pphub14160250290.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

def read_text_from_file(file_path):
    """Read text content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    ) 

    document = [text]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    # Read text from input file
    input_text = read_text_from_file('input.txt')

    if input_text:
        print("\nAnalyzing text from input.txt...")
        language_detection_example(client, input_text)

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: {}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences])
            ))

sample_extractive_summarization(client)
