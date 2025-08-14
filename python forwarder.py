from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest

# ===== CONFIG =====
api_id = 27849705
api_hash = '3538e75ae408e3837fc91133cc1ee51b'
source_channel = 'FourMemeAlert'  # without @
target_chat = -1002654235459
# ===================

# Create Telegram client session
client = TelegramClient('forward_session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_handler(event):
    try:
        await client.send_message(target_chat, event.message)
        print(f"[FORWARDED] {event.message.id}")
    except Exception as e:
        print(f"[ERROR] {e}")

async def main():
    # Try to join channel if not already joined
    try:
        await client(JoinChannelRequest(source_channel))
        print(f"Joined channel: {source_channel}")
    except Exception:
        print(f"Already joined channel or failed to join.")

    print("Forwarder is running... Waiting for new messages.")

# Start the userbot
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
