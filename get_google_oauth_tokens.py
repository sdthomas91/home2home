import os
import json
import google.oauth2.credentials
import google_auth_oauthlib.flow

# Load client secrets from environment variables
CLIENT_SECRETS = {
  "web": {
    "client_id": os.getenv("OAUTH_CLIENT_ID"),
    "project_id": os.getenv("OAUTH_PROJECT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": os.getenv("OAUTH_CLIENT_SECRET")
  }
}

# The OAuth 2.0 scopes required by this app
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Create the flow using the client secrets from environment variables
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config(
    CLIENT_SECRETS, SCOPES)

# Run the flow to get credentials
credentials = flow.run_local_server(port=0)

print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)
