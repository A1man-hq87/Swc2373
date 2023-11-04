import requests
import json
#String Tokenizer will reset every 12hours 
base_url = "https://api.ciscospark.com/v1" #WEBEX SPI LINK
access_token = input("Please enter your Webex access token: ")#Please Enter The user webex Token to access user data in webex server 
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

res = requests.get(base_url, headers=headers)

#Test connection by using toknennizer from webex 
def test_connection():
    response = requests.get(f"{base_url}/people/me", headers=headers)
    if response.status_code == 200:
        print("Connection to Webex server successful.")
    else:
        print("Connection to Webex server failed.")
    input("Press Enter to return.")

#User information  
def display_user_info():
    response = requests.get(f"{base_url}/people/me", headers=headers)
    if response.status_code == 200:
        user_info = json.loads(response.text)
        print("User Information:")
        print(f"Display Name: {user_info['displayName']}")
        print(f"Nickname: {user_info['nickName']}")
        print("Emails:")
        for email in user_info['emails']:
            print(email)
    input("Press Enter to return.")

#ROOM INFORMATION
def list_rooms():
    response = requests.get(f"{base_url}/rooms", headers=headers)#Get Room Information and run it 
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("List of Rooms:")
        for room in rooms['items'][:5]:
            print(f"Room ID: {room['id']}")
            print(f"Room Title: {room['title']}")
            print(f"Create Date: {room['created']}")
            print(f"Recent Activity: {room['lastActivity']}")
            print()
    input("Press Enter to return.")

#CREATE NEW ROOM
def create_room():
    room_title = input(
        "Please Enter Room Name: "
        )
    room_data = {
        "title": room_title
        }
    response = requests.post(f"{base_url}/rooms", headers=headers, json=room_data)
    if response.status_code == 200:
        print("Room created successfully.")
    else:
        print("Failed to create a room.")
    input("Press Enter to return.")

#SEND MESSAGE TO ROOM 
def send_message():
    response = requests.get(f"{base_url}/rooms", headers=headers)
    if response.status_code == 200:
        rooms = json.loads(response.text)
        print("Select a room to send a message:")
        for i, room in enumerate(rooms['items'][:5]):
            print(f"{i}. {room['title']}")

        room_index = int(input("Enter the room ID: "))
        if 0 <= room_index < 5:
            room_id = rooms['items'][room_index]['id']
            message = input("Enter the message: ")
            message_data = {"roomId": room_id, "text": message}
            response = requests.post(f"{base_url}/messages", headers=headers, json=message_data)
            if response.status_code == 200:
                print("Message sent successfully.")
            else:
                print("Failed to send the message.")
    input("Press Enter to return.")

#MAIN INTERFACES
while True:
    print("Webex TroubleShooting center:")
    print("0. Test Connection with webex")
    print("1. Display all User Information")
    print("2. All Room information")
    print("3. Create a Room")
    print("4. Send Message to a Room")
    print("5. Exit")
    
    option = input("Please select an option: ")
    
    if option == "0":
        test_connection()
    elif option == "1":
        display_user_info()
    elif option == "2":
        list_rooms()
    elif option == "3":
        create_room()
    elif option == "4":
        send_message()
    elif option == "5":
        print("Loging Out. Have A nice Day")
        break
    else:
        print("Failed to pick an option. Please choose the correct option.")
