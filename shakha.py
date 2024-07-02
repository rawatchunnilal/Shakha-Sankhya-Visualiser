import re
from datetime import datetime
import pandas as pd

# Path to the uploaded WhatsApp chat file
file_path = 'WhatsApp Chat with 🚩गणेशनगर सायम शाखा🚩.txt'

def parse_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into messages using the date and time as separator
    messages = re.split(r'\n(?=\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[AP]M\s-\s)', content)

    # Remove any leading/trailing whitespace from messages
    messages = [msg.strip() for msg in messages if msg.strip()]

    return messages

def format_message(message):
    # Extract the date, time, and content from the message
    match = re.match(r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s*[AP]M)\s-\s(.*)', message, re.DOTALL)
    if match:
        datetime_str, content = match.groups()
        # Replace non-ASCII characters with a standard space
        datetime_str = re.sub(r'[^\x00-\x7F]+', ' ', datetime_str)
        # Try parsing with both 2-digit and 4-digit year formats
        try:
            dt = datetime.strptime(datetime_str, '%m/%d/%y, %I:%M %p')
        except ValueError:
            try:
                dt = datetime.strptime(datetime_str, '%m/%d/%Y, %I:%M %p')
            except ValueError:
                return {'date_time': None, 'author': None, 'message': f"Unable to parse date: {datetime_str}\n{content}"}
        formatted_dt = dt.strftime('%Y-%m-%d %H:%M')
        # Check if it's a system message or a user message
        if ': ' in content:
            author, text = content.split(': ', 1)
            return {'date_time': formatted_dt, 'author': author, 'message': text}
        else:
            return {'date_time': formatted_dt, 'author': 'System', 'message': content}
    return {'date_time': None, 'author': None, 'message': message}


# Parse the chat
distinct_messages = parse_messages(file_path)

# Format messages and collect them in a list
formatted_messages = [format_message(msg) for msg in distinct_messages]

# Create a DataFrame
df = pd.DataFrame(formatted_messages, columns=['date_time', 'author', 'message'])

# Display the DataFrame
df
