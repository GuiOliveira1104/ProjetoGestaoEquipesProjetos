import requests

# Replace the placeholders with your Trello API key and authorization token
api_key = ''
auth_token = ''

def get_boards():
    # Define the endpoint for retrieving the boards
    endpoint = 'https://api.trello.com/1/members/me/boards'

    # Set the parameters for the request
    params = {
        'key': api_key,
        'token': auth_token
    }

    # Send the GET request to retrieve the boards and retrieve the response
    response = requests.get(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Get the boards data from the response
        boards = response.json()

        # Print the name of each board
        for board in boards:
            print(board['name'])
    else:
        # Print an error message
        print('An error occurred while retrieving the boards:', response.text)

def get_lists(board_id):
    # Define the endpoint for retrieving the lists
    endpoint = f'https://api.trello.com/1/boards/{board_id}/lists'

    # Set the parameters for the request
    params = {
        'key': api_key,
        'token': auth_token
    }

    # Send the GET request to retrieve the lists and retrieve the response
    response = requests.get(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Get the lists data from the response
        lists = response.json()

        # Print the name of each list
        for trello_list in lists:
            print(trello_list['name'])
    else:
        # Print an error message
        print('An error occurred while retrieving the lists:', response.text)

def get_cards(list_id):
    # Define the endpoint for retrieving the cards
    endpoint = f'https://api.trello.com/1/lists/{list_id}/cards'

    # Set the parameters for the request
    params = {
        'key': api_key,
        'token': auth_token
    }

    # Send the GET request to retrieve the cards and retrieve the response
    response = requests.get(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Get the cards data from the response
        cards = response.json()

        # Print the name of each card
        for card in cards:
            print(card['name'])
    else:
        # Print an error message
        print('An error occurred while retrieving the cards:', response.text)


def insert_card(list_id, name, description=None):
    # Define the endpoint for creating a card
    endpoint = f'https://api.trello.com/1/cards'

    # Set the parameters for the request
    params = {
        'key': api_key,
        'token': auth_token,
        'idList': list_id,
        'name': name,
        'desc': description
    }

    # Send the POST request to create the card and retrieve the response
    response = requests.post(endpoint, data=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Get the card data from the response
        card = response.json()

        # Print a success message
        print(f'The card "{card["name"]}" was created successfully.')
    else:
        # Print an error message
        print('An error occurred while creating the card:', response.text)

def delete_card(card_id):
    # Define the endpoint for deleting a card
    endpoint = f'https://api.trello.com/1/cards/{card_id}'

    # Set the parameters for the request
    params = {
        'key': api_key,
        'token': auth_token
    }

    # Send the DELETE request to delete the card and retrieve the response
    response = requests.delete(endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Print a success message
        print(f'The card with ID {card_id} was deleted successfully.')
    else:
        # Print an error message
        print('An error occurred while deleting the card:', response.text)
# Print a menu of options
print('Trello CLI')
print('1. View boards')
print('2. View lists')
print('3. View cards')

print('4. Exit')
