import smtplib
import ssl
from email.message import EmailMessage
import sys

# --- Configuration ---
sender_email = "notification@apigoo-syd.lycamobile.com.au"
recipient_email = "Palash.Paul2@example.com"
smtp_server = "smtp.email.ap-sydney-1.oci.oraclecloud.com"
smtp_port = 465  # SSL port
username = "ocid1.user.oc1..aaaaaaaaawwn4jifiejeeqjvgtz63va3tqkubf2ada2okhnbojdmig4rzdga@ocid1.tenancy.oc1..aaaaaaaansmpcdmysic6h5l3zencs5kyirgy47lpmh2jz5rtggd3euy2kbza.9d.com"
password = "xxxxxx"

# --- Create the email message ---
message = EmailMessage()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "SMTP Gateway Test"
message.set_content(f"""
This is a test email sent via Python to verify the SMTP gateway configuration.

Server: {smtp_server}
Port: {smtp_port}
Username: {username}
""")

# --- Send the email using SSL ---
context = ssl.create_default_context()

print(f"Attempting to connect to {smtp_server}:{smtp_port} using SSL...")

try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=30) as server:
        print("SSL connection established.")
        print(f"Logging in as {username}...")
        server.login(username, password)
        print("Login successful.")
        print(f"Sending test email to {recipient_email}...")
        server.send_message(message)
        print("Email sent successfully!")
except smtplib.SMTPAuthenticationError as e:
    print(f"SMTP Authentication Error: Could not log in. Check username/password. ({e})")
except smtplib.SMTPConnectError as e:
    print(f"SMTP Connection Error: Failed to connect to the server. ({e})")
except smtplib.SMTPServerDisconnected as e:
    print(f"SMTP Server Disconnected: The server unexpectedly disconnected. ({e})")
except smtplib.SMTPException as e:
    print(f"SMTP Error: An SMTP error occurred: {e}")
except ssl.SSLError as e:
    print(f"SSL Error: An SSL error occurred during negotiation: {e}")
except ConnectionRefusedError as e:
    print(f"Connection Refused Error: The server refused the connection. Check server address/port and firewall rules. ({e})")
except TimeoutError as e:
    print(f"Timeout Error: Connection attempt timed out. Check network connectivity and server status. ({e})")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
