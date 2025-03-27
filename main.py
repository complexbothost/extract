import requests

def fetch_json_from_url(url):
    try:
        # Sending a GET request to the specified URL
        response = requests.get(url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Attempt to parse the response as JSON
        json_data = response.json()
        
        # Display the JSON data
        print("JSON Response:")
        print(json_data)
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # e.g., network problem
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # e.g., request timed out
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")  # Catch-all for other request-related errors
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")  # Handle JSON decoding errors

# Example usage
if __name__ == "__main__":
    url = input("https://api.example.com/data")  # Replace with the actual URL
    fetch_json_from_url(url)
