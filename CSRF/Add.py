import requests

# Define the URL for adding a new contact
url = 'http://127.0.0.1:8000/contact/create/'

# Use the actual session ID and CSRF token from your message

#User
session_id = 'jftcel8rasex0fevf5xek5fsop87d57r' 
csrf_token = '7qWkhnE8gNOSFz3i15fPosPFffEFGIVe'       

#Admin       
#session_id = '2i3a3r24lpctiujsfguoisejc234dqml' 
#csrf_token = 'HwhrQNFU6Lwrd7U2qwVk53RkTxl8AwFs'  

# Define the headers (include all necessary headers observed in Developer Tools)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'http://127.0.0.1:8000/contact/create/',
    'X-CSRFToken': csrf_token,
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Define the cookies to include both the session ID and the CSRF token
cookies = {
    'sessionid': session_id,
    'csrftoken': csrf_token
}

# Define the payload with the contact details
payload = {
    'first_name': 'AHA!',
    'last_name': 'U GOT TRICK',
    'phone_number': '000000000',
    'csrfmiddlewaretoken': csrf_token  # Include this if necessary in the payload
}

# Send the POST request
response = requests.post(url, headers=headers, cookies=cookies, data=payload)

# Print response details for debugging
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# Check if the contact was added successfully
if response.status_code == 200:
    print("Contact added successfully!")
else:
    print("Failed to add contact.")
