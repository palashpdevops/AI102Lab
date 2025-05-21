
from dotenv import load_dotenv
import os
import http.client, base64, json, urllib
from urllib import request, parse, error

def main():
    global ai_endpoint
    global ai_key

    try:
        load_dotenv()
        ai_endpoint = os.getenv('AI_Service_Endpoint')
        ai_key = os.getenv('AI_Service_Key')

        userText =''
        while userText.lower() != 'quit':
            userText = input('Enter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                GetLanguage(userText)
                print(userText)
    except Exception as ex:
        print(ex)
  def GetLanguage(text):
      try:
          jsonbody = {
              "Documents":[
                  {"id": 1
                   "text": text
                  }
              ]
          }
        print(json.dumps(jsonBody, index=2))
        uri = ai_endpoint.rstrip('/').replace('https://', '')
        conn = http.client.HTTPSConnection(uri)

        headers = {   
          'Content-Type': 'application/json',
          'Ocp-Apim-Subscription-Key': ai_key
        }
       conn.request("POST", "/text/analytics/v3.1/languages?", str(jsonBody).encode('utf-8'), headers)

        # Send the request
        response = conn.getresponse()
        data = response.read().decode("UTF-8")

       # If the call was successful, get the response        
        if response.status == 200:
            # Display the JSON response in full (just so we can see it) 
            results = json.loads(data)
            print(json.dumps(results, indent=2))            
              # Extract the detected language name for each document
              for document in results["documents"]:
                  print("\nLanguage:", document["detectedLanguage"]["name"]) 
        else:
            # Something went wrong, write the whole response            
            print(data)        
        conn.close()    
        except Exception as ex:
            print(ex)

if __name__ == "__main__":
    main()


==========================
Create a .env file
AI_SERVICE_ENDPOINT='AI_Service_Endpoint'
AI_SERVICE_KEY='AI-Service-Key'

