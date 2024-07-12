import os
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow

# Path to client_secrets.json file downloaded from the Google API Console
CLIENT_SECRETS_FILE = "client_secret.json"

# The OAuth 2.0 scopes required by this app
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Create the flow using the client secrets file
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE, SCOPES)

# Run the flow to get credentials
credentials = flow.run_local_server(port=0)

print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)
