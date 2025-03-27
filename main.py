import requests
import csv
import os

def fetch_json_data(user):
    """Fetch JSON data from the specified URL."""
    url = f"https://guns.lol/{user}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")
    return None

def save_to_csv(data, filename):
    """Save the extracted data to a CSV file."""
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(data[0].keys())
            # Write data rows
            for item in data:
                writer.writerow(item.values())
        print(f"Data successfully saved to {filename}")
    except IOError as io_err:
        print(f"IO error occurred: {io_err}")

def main(user):
    """Main function to execute the extraction and saving process."""
    json_data = fetch_json_data(user)
    if json_data:
        csv_filename = f"{user}_data.csv"
        save_to_csv(json_data, csv_filename)
    else:
        print("No data fetched. Please check the user or the URL.")

if __name__ == "__main__":
    user_input = input("Enter the username: ")
    main(user_input)
