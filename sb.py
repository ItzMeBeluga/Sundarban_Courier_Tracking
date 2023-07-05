import requests
import json

# Function to make a POST request to the API
def make_post_request(url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# API URLs
tracking_api_url = "https://tracking.sundarbancourierltd.com/Home/getDatabyCN"
master_details_api_url = "https://tracking.sundarbancourierltd.com/Home/GetMasterDetails"

# Prompt for selected type input
print("Please select the desired type from the options:")
print("1. Reciever Contact (receiverno)")
print("2. CN Number (cnno)")
print("3. Sender Contact (senderno)")
print("4. Reference No. (refno)")

selected_type = input("Enter your choice (1-4): ")

# Prompt for selected times input
selected_times = input("Please enter the Days Range of Tracking(7,14,21,30 Days): ")

# Prompt for input value based on selected type
if selected_type == "1":
    input_value = input("Please enter Receiver Contact: ")
elif selected_type == "2":
    input_value = input("Please enter CN Number: ")
elif selected_type == "3":
    input_value = input("Please enter Sender Contact: ")
elif selected_type == "4":
    input_value = input("Please enter Reference No.: ")
else:
    print("Invalid choice!")
    exit()

# Create the payload for the tracking API
payload_tracking = {
    "selectedtypes": "receiverno" if selected_type == "1" else "cnno" if selected_type == "2" else "senderno" if selected_type == "3" else "refno",
    "selectedtimes": selected_times,
    "inputvalue": input_value
}

# Make a request to the tracking API
response_tracking = make_post_request(tracking_api_url, payload_tracking)
print("Response from Tracking API:")
print(json.dumps(response_tracking, indent=4))

# Prompt for master details
master_details_input = input("If you want Masterdetails of this CN, press Enter: ")

if master_details_input == "" and isinstance(response_tracking, list) and len(response_tracking) > 0:
    # Extract cnFrom value from the first object in the response list
    cn_from = response_tracking[0].get("cnFrom")

    # Create the payload for the master details API
    payload_master_details = {
        "cnnumber": cn_from
    }

    # Make a request to the master details API
    response_master_details = make_post_request(master_details_api_url, payload_master_details)
    print("Response from Master Details API:")
    print(json.dumps(response_master_details, indent=4))
