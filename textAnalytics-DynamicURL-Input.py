from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    """Extract text content from a given URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        print(f"Error fetching URL content: {e}")
        return None

def analyze_text(text, endpoint, key):
    """Analyze text using Azure Text Analytics"""
    try:
        # Authenticate the client
        credential = AzureKeyCredential(key)
        text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
        
        # Analyze sentiment
        sentiment_result = text_analytics_client.analyze_sentiment([text])[0]
        
        # Extract key phrases
        key_phrases_result = text_analytics_client.extract_key_phrases([text])[0]
        
        # Recognize entities
        entities_result = text_analytics_client.recognize_entities([text])[0]
        
        return {
            'sentiment': sentiment_result.sentiment,
            'confidence_scores': sentiment_result.confidence_scores,
            'key_phrases': key_phrases_result.key_phrases,
            'entities': [entity.text for entity in entities_result.entities]
        }
    except Exception as e:
        print(f"Error analyzing text: {e}")
        return None

def main():
    # Azure Text Analytics credentials
    endpoint = "YOUR_AZURE_TEXT_ANALYTICS_ENDPOINT"  # e.g., "https://your-resource-name.cognitiveservices.azure.com/"
    key = "YOUR_AZURE_TEXT_ANALYTICS_KEY"
    
    # Prompt user for URL
    url = input("Please enter the URL you want to analyze: ").strip()
    
    # Get text from URL
    print(f"\nFetching content from: {url}")
    text = get_text_from_url(url)
    
    if not text:
        print("Failed to extract text from the URL.")
        return
    
    print(f"\nExtracted {len(text)} characters from the URL.")
    
    # Analyze the text
    print("\nAnalyzing content with Azure Text Analytics...")
    analysis_results = analyze_text(text, endpoint, key)
    
    if not analysis_results:
        print("Failed to analyze the text.")
        return
    
    # Display results
    print("\nAnalysis Results:")
    print(f"Sentiment: {analysis_results['sentiment']}")
    print(f"Positive Score: {analysis_results['confidence_scores'].positive:.2f}")
    print(f"Neutral Score: {analysis_results['confidence_scores'].neutral:.2f}")
    print(f"Negative Score: {analysis_results['confidence_scores'].negative:.2f}")
    
    print("\nKey Phrases:")
    for phrase in analysis_results['key_phrases']:
        print(f"- {phrase}")
    
    print("\nRecognized Entities:")
    for entity in analysis_results['entities']:
        print(f"- {entity}")

if __name__ == "__main__":
    main()


###############################################
How to Use This Code:
Replace YOUR_AZURE_TEXT_ANALYTICS_ENDPOINT and YOUR_AZURE_TEXT_ANALYTICS_KEY with your actual Azure credentials.
Required Python packages:
azure-ai-textanalytics
requests
beautifulsoup4

Install them with:
pip install azure-ai-textanalytics requests beautifulsoup4
  
