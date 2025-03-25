

#Fallow me on:
#https://T.me/AiHoma
#https://github.com/Aihoma
#https://medium.com/@AiHoma


from telethon import TelegramClient, functions, types
import asyncio

# Telegram API credentials
api_id = 'YOUR_API_ID'  # Replace with your Telegram API ID
api_hash = 'YOUR_API_HASH'  # Replace with your Telegram API Hash
phone_number = 'YOUR_PHONE_NUMBER'  # Replace with your phone number

# Create a Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def delete_all_chats_with_deleted_accounts_and_bots():
    """
    Deletes all chats with deleted accounts and bots from your Telegram account.
    """
    # Start the client and log in
    await client.start(phone=phone_number)
    print("Client started. Fetching dialogs...")

    # Keep checking until all relevant chats are deleted
    keep_checking = True
    while keep_checking:
        keep_checking = False  # Reset the flag for each iteration
        dialogs = await client.get_dialogs()  # Fetch all dialogs (chats)

        for dialog in dialogs:
            # Check if the dialog is with a user (not a group or channel)
            if isinstance(dialog.entity, types.User):
                user = await client.get_entity(dialog.entity.id)  # Get user details

                # Check if the user is deleted or a bot
                if user.deleted or user.bot:
                    try:
                        # Delete the chat history with the deleted account or bot
                        await client(functions.messages.DeleteHistoryRequest(
                            peer=dialog.entity,
                            max_id=0,  # 0 means delete the entire chat history
                            just_clear=False,  # False means delete the chat completely
                            revoke=True  # Revoke the chat for both sides
                        ))
                        print(f"✅ Successfully removed chat with: {dialog.entity.id} (Deleted: {user.deleted}, Bot: {user.bot})")
                        keep_checking = True  # Re-check to ensure all chats are processed
                    except Exception as e:
                        print(f"❌ Failed to remove chat with {dialog.entity.id}: {e}")

    # Disconnect the client after completing the task
    await client.disconnect()
    print("Client disconnected. All relevant chats have been processed.")

# Run the script
if __name__ == "__main__":
    asyncio.run(delete_all_chats_with_deleted_accounts_and_bots())