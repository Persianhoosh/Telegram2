
# Remove-All-Delete-account-and-Bot-Telegram

## How to Use :

1. Install Dependencies:
   Make sure you have the telethon library installed. You can install it using pip:
                        
**bash**
  
  ╰─➢ pip install telethon
==================================
  
2. Replace Placeholder Values:
   
    ✅YOUR_API_ID
   
    ✅YOUR_API_HASH
   
    ✅+YOUR_PHONE_NUMBER
   
      with your actual Telegram API credentials and phone number.
    
3.Run the Script:
  
**bash**
  
  ╰─➢ python Delete.py
===================================

## Notes

API Credentials:
Obtain your API ID and API Hash from my.telegram.org.

Session File:
The script creates a session_name.session file to store your login session. Keep this file secure.

Permissions:
If you’re an admin in a group, you may need to resign as admin before leaving.

Use with Caution:
This script leaves all groups and channels. Use it carefully.

A Python script to automatically delete all chats with deleted accounts and bots on Telegram.

## Features
- Detects and deletes chats with deleted accounts.
- Detects and deletes chats with bots.
- Uses the Telethon library to interact with the Telegram API.

## Requirements
- Python 3.7+
- Telethon library

__________________________________________
