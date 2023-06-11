
'''
Generate the urlencoded text to be used in WhatsApp Link:-
1. Type the text that you want to send via WhatsApp
2. Run this code and copy the output.
3. Paste it in the WhatsApp "link" variable in whatsapp.py 
'''

import urllib.parse

text = """Hey, 

This is Demo Text.

Thanks!"""

encoded_text = urllib.parse.quote(text)
print(encoded_text)