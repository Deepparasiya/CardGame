import requests

# API URL
URL = "https://labs.cyberwarfare.live/api/user/course/module/flag/check"

# Headers (Replace with your actual token if needed)
Headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNjc0NzAzYTNkMjgyZTA3N2JhNjg5ZjVkIiwiaWF0IjoxNzM0MTc5NTA3LCJleHAiOjE3MzQzNTIzMDd9.RgF7y9qLk3NDUJdjDv_fx2tGwWP80D87id5h4A7-6R4",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0)",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://labs.cyberwarfare.live",
    "Referer": "https://labs.cyberwarfare.live/app/mycourse/mcrta/modules/GCP%20Cloud%20Red%20Teaming",
}

# Cookies (Replace values with actual if needed)
cookies = {
    'Cookie': 'user=%7B%22user_id%22%3A%22674703a3d282e077ba689f5d%22%2C%22usename%22%3A%22eklavya%22%2C%22email%22%3A%22deepparasiya54%40gmail.com%22%2C%22user_image%22%3A%22%22%2C%22token%22%3A%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiNjc0NzAzYTNkMjgyZTA3N2JhNjg5ZjVkIiwiaWF0IjoxNzM0MTc5NTA3LCJleHAiOjE3MzQzNTIzMDd9.RgF7y9qLk3NDUJdjDv_fx2tGwWP80D87id5h4A7-6R4%22%7D'
}

# Data payload template
data_template = {
    "module_id": "65c9bca329623e31c14f961c",
    "course_name": "mcrta",
    "flag_id": "65d4be576692ab4daa05d5aa"
}

# File containing emails
input_file = "emails.txt"  # Replace with your file name

# Read emails from the file
try:
    with open(input_file, 'r') as file:
        emails = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
    exit()

# Loop through emails and send requests
for email in emails:
    data = data_template.copy()
    data["answer"] = email  # Set the email as the answer parameter

    try:
        response = requests.post(URL, headers=Headers, json=data, cookies=cookies)

        # Print the response for each email
        print(f"Email: {email} | Response: {response.status_code} | {response.json()}\n")
    except ValueError:
        print(f"Email: {email} | Response: {response.status_code} | Failed to parse JSON. Raw response: {response.text}\n")
    except Exception as e:
        print(f"Email: {email} | Error: {str(e)}\n")
