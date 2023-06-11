'''
Before running this file, do these changes:-
1. Enter the directory path of csv file (line 15)
2. Replace text variable with text generated from urlencoded_text.py (line 47)
3. Replace mouse coordinates generated from mouse_coordinates.py (line 55 and 59)
'''

# Import Python Dependencies
import os
import time
import pyautogui
import pandas as pd

# Create a directory's url and change the csv file name to data.csv
dir_path = 'ENTER YOUR DIRECTORY PATH HERE'                                         # Path of directory from your system
files = os.listdir(dir_path)                                                        # List of all files in the directory
for file_name in files:                                                             # For each file name there
  if '.csv' in file_name:                                                           # If .csv present in the name
   os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, 'data.csv')) # Replace it with data.csv

# Data extraction 
data = pd.read_csv(f'{dir_path}data.csv')            # Read csv file
cols = list(data.columns)                            # Get the column titles/names
names_numbers_col_title = []                         # Empty list to store title of col for name and number in same order
for col in cols:                                     # For each column 
    if 'name' in col:                                # If name is present in the column name
        names_numbers_col_title.append(col)          # Append that column title to the empty list to store it on index 0
    if ('phone' or 'number') in col:                 # If phone or number is present in the column name
        names_numbers_col_title.append(col)          # Append that column title to the names_numbers_col_title on index 1

# Data engineering with the name and number col in data
names = [name.title().replace(' ', '%20') for name in list(data[f'{names_numbers_col_title[0]}'])] # Extract Names 
numbers = data[f'{names_numbers_col_title[1]}'].values.astype('str')                               # Extract Numbers
for idx, number in enumerate(numbers):          # For ever number                                  
    if number[:2] == '91':                      # If first two digits are 91
        if len(number) == 10:                   # And if total length is 10
            numbers[idx] = f'91{number}'        # Add country code of India
    else:                                       # If first two digits aren't 91
        numbers[idx] = f'91{number}'            # Add country code of India
        assert len(number) != 12                # Raise Assertation if total digits of a number is not 12


# WhatsApp Simulation to automatically send the message
for i in range(len(numbers)):        # For each number and name 

    # Use urlencoded_text.py to convert your text into encoded_text and create whatsapp link 
    text = f"Hello%20{names[i]}%2C%0A%0AThis%20is%20a%20reminder%20to%20join%20the%20Slack%20workspace%20to%20get%20access%20to%20the%20live%20sessions%20link%2C%20content%2C%20recordings%2C%20e.t.c.%20We%20have%20sent%20you%20this%20Slack%20invitation%20on%20your%20registered%20email-id.%0A%0APlease%20reply%20back%20in%20case%20of%20any%20confusions%20or%20not%20able%20to%20sign%20in%20to%20the%20workspace.%0A%0AThank%20you.%0A%0ARegards%2C%0ARohan%2C%0AFundamentals%20of%20Astrodynamics%20with%20Python%20%28Spartificial%29"
    link = f"https://wa.me/{numbers[i]}?text={text}"  # WhatsApp Link with Number and Text

    # Set your mouse coordinates to start chat and use whatsapp web locations on chrome and exit whatsapp once msg sent
    os.system(f"start chrome {link}")  # Initiate Chrome with WhatsApp link
    time.sleep(2)                      # Give 2 seconds time to open 
    
    # Adjust coordinates acc to your screen size using mouse_coordinates.py
    pyautogui.click(x=942, y=325)      # Click on Continue to Chat Button on Chrome
    time.sleep(2)                      # 2 seconds pause

    # Adjust coordinates acc to your screen size using mouse_coordinates.py
    pyautogui.click(x=962, y=392)      # Click on With WhatsAppWeb Button on Chrome
    time.sleep(8)                      # 8 seconds pause


    pyautogui.press('enter')           # Send the message automatically
    time.sleep(1)                      # 1 second pause

    pyautogui.hotkey('ctrl', 'w')      # Close the WhatsApp Tab / Current Tab