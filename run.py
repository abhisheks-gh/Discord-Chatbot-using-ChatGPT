# To test the functionality
from app.discord_bot.discord_api import client, discord_token

# Checks whether the code is been run as the main program or 
# if it's been imported as a module
if __name__ == '__main__':
    client.run(discord_token)