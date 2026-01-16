import requests
import json

# Replace the placeholders with your Trello API key and authorization token
api_key = ''
auth_token = ''

# Define the endpoint for the request
endpoint = 'https://api.trello.com/1/members/me/boards'

# Set the parameters for the request
params = {
    'key': api_key,
    'token': auth_token
}

# Send the GET request and retrieve the response
response = requests.get(endpoint, params=params)

# Check the status code of the response
if response.status_code == 200:
    # Print the JSON data from the response
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
else:
    # Print an error message
    print('An error occurred:', response.text)

