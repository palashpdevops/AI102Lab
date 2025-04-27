##############
#Key phrase extraction is a capability provided by Azure AI Language, a suite of machine learning and AI tools designed for building intelligent applications that process and understand written language.
#This feature helps you rapidly pinpoint the key ideas within a piece of text.
#For instance, given the text "The hotel room was clean and the location was perfect.", key phrase extraction would highlight the main topics: "hotel room" and "perfect location".
################

#-------------------------------------------------------
#Code Section 
#--------------------------------------------------------
import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client
def authenticate_client():
    ta_credential = AzureKeyCredential("1P7XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXJ3w3AAAaACOG0VGw")
    text_analytics_client = TextAnalyticsClient(
        endpoint="https://project1language.cognitiveservices.azure.com/",
        credential=ta_credential
    )
    return text_analytics_client

client = authenticate_client()

# Key Phrase Extraction
def key_phrase_extraction_example(client):
    try:
        documents = [
            "AEM Institute is a AI Training Institute located in South Kolkata near Lake Mall."
        ]

        response = client.extract_key_phrases(documents=documents)

        for idx, doc in enumerate(response):
            if not doc.is_error:
                print(f"\nDocument {idx + 1} Key Phrases:")
                for phrase in doc.key_phrases:
                    print(f"  - {phrase}")
            else:
                print(f"\nDocument {idx + 1} has error: {doc.error}")

    except Exception as err:
        print(f"Encountered exception: {err}")

# Run the example
key_phrase_extraction_example(client)
---------------------------------------------------
####
    1  apt-get update -y
    2  mkdir application
    3  cd application/
    4  ls -lrt
    5  apt install python3-pip
    6  apt install python3-venv -y
    7  python3 -m venv myvenv
    8  source myvenv/bin/activate
    9  pip install --upgrade
   10  pip install --upgrade pip
   11  pip install --upgrade az
   12  pip install pillow
   13  touch app.py
   14  vi app.py 
   15  python app.py 
   16  pip install azure-ai-textanalytics
   17  python app.py 
####################################
