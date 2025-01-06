import csv
import re

# Ask for the input file path
input_file_path = input("Enter the path to the input text file (e.g., 'result.txt'): ")
output_file_path = 'result.csv'

# Define patterns to capture relevant information
patterns = {
    'type': r'\[([^\]]+)\]',  # Capture the type in square brackets (e.g., [dns-waf-detect:cloudflare])
    'category': r'\[([^\]]+)\]\s+\[([^\]]+)\]\s+\[([^\]]+)\]',  # Capture category (e.g., [info], [high], etc.)
    'url': r'(https?://[^\s]+)',  # Capture URLs (https:// or http://)
    'hostname': r'([a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,}))',  # Capture the hostname (domain) or IP address
    'additional_info': r'\["([^"]+)"\]'  # Capture additional details in quotes (e.g., IDs)
}

# List to store extracted data
extracted_data = []

# Function to parse each line
def parse_line(line):
    data = {}

    # Try to match the type
    match_type = re.search(patterns['type'], line)
    if match_type:
        data['type'] = match_type.group(1)
    else:
        data['type'] = 'N/A'  # Use 'N/A' if no type found

    # Try to match the category
    match_category = re.search(patterns['category'], line)
    if match_category:
        data['category'] = match_category.group(3)  # The severity is in the third capture group
    else:
        data['category'] = 'N/A'  # Use 'N/A' if no category found

    # Try to match the URL
    match_url = re.search(patterns['url'], line)
    if match_url:
        data['url'] = match_url.group(1)
    else:
        data['url'] = 'N/A'  # Use 'N/A' if no URL found

    # Try to match the hostname
    match_hostname = re.search(patterns['hostname'], line)
    if match_hostname:
        data['hostname'] = match_hostname.group(1)
    else:
        data['hostname'] = 'N/A'  # Use 'N/A' if no hostname found

    # Try to match additional info
    match_additional_info = re.findall(patterns['additional_info'], line)
    if match_additional_info:
        data['additional_info'] = ", ".join(match_additional_info)
    else:
        data['additional_info'] = 'N/A'  # Use 'N/A' if no additional info found

    return data

# Read the input file and process each line
try:
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parsed_data = parse_line(line)
        extracted_data.append(parsed_data)

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
    exit(1)

# Write the extracted data to a CSV file
try:
    with open(output_file_path, 'w', newline='') as csvfile:
        fieldnames = ['type', 'category', 'url', 'hostname', 'additional_info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in extracted_data:
            writer.writerow(data)

    print(f"Process completed successfully. Results saved in '{output_file_path}'.")

except Exception as e:
    print(f"An error occurred while writing the CSV file: {e}")
