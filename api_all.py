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
    boards_data = response.json()

    # Loop through each board
    for board in boards_data:
        # Get the ID of the board
        board_id = board['id']

        # Define the endpoint for retrieving the lists
        lists_endpoint = f'https://api.trello.com/1/boards/{board_id}/lists'

        # Set the parameters for the request
        lists_params = {
            'key': api_key,
            'token': auth_token
        }

        # Send the GET request to retrieve the lists and retrieve the response
        lists_response = requests.get(lists_endpoint, params=lists_params)

        # Check the status code of the response
        if lists_response.status_code == 200:
            # Get the lists data from the response
            lists_data = lists_response.json()

            # Loop through each list
            for trello_list in lists_data:
                # Get the ID of the list
                list_id = trello_list['id']

                # Define the endpoint for retrieving the cards
                cards_endpoint = f'https://api.trello.com/1/lists/{list_id}/cards'

                # Set the parameters for the request
                cards_params = {
                    'key': api_key,
                    'token': auth_token
                }

                # Send the GET request to retrieve the cards and retrieve the response
                cards_response = requests.get(cards_endpoint, params=cards_params)

                # Check the status code of the response
                if cards_response.status_code == 200:
                    # Get the cards data from the response
                    cards_data = cards_response.json()

                    # Loop through each card
                    for card in cards_data:
                        # Print the name of the card
                        print(card['name'])
                else:
                    # Print an error message
                    print('An error occurred while retrieving the cards:', cards_response.text)
        else:
            # Print an error message
            print('An error occurred while retrieving the lists:', lists_response.text)
else:
    # Print an error message
    print('An error occurred:', response.text)

