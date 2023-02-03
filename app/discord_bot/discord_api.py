# load_dotenv imports our environment variables placed within the .env file
from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

# Load environment variables placed within .env file
load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print("Succesfully logged in: ", self.user)

    async def on_message(self, message):
        # Prints content of the message to the console
        print(message.content)
        # Prevents the bot itself to reply to its own message
        if message.author == self.user:
            return
        # Command to call the bot and save their message
        command, user_message = None, None
        for text in ['/ai', '/bot', '/chatgpt']:
            # Spliting 
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
                print(command, user_message)
        
        if command == '/ai' or command == '/bot' or command == '/chatgpt':
            bot_response = chatgpt_response(prompt = user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content = True

# Creating an instance of this class
client = MyClient(intents = intents)