from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

SCOPES = ["https://www.googleapis.com/auth/blogger"]

flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

creds = flow.run_local_server(host="127.0.0.1", port=8080, open_browser=False)

with open("token.pickle", "wb") as f:
    pickle.dump(creds, f)

print("تم إنشاء token.pickle")
