from pyrogram import Client, filters
from os import environ


# Configuration - replace with your own values
api_id = environ.get("api_id", "")
api_hash = environ.get("api_hash", "")
bot_token = environ.get("bot_token", "")


# Initialize the bot
app = Client(
    "my_bot",
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token
)

# Define a handler for photo and video messages
@app.on_message(filters.photo | filters.video)
def thanks(client, message):
    message.reply_text("Thanks for posting , send more sex videos or hot  photo 😘

Any way if you want to fuck me just write yes !!")

# Run the bot
app.run()
