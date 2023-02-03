# Discord-Chatbot-using-ChatGPT

## Installing requirements
    requirements.txt contains the list of all requirements and to install them:
    Go to Project_Location -> Open CMD -> Run below mentioned command
    pip install -r requirements.txt

## Generate ChatGPT API key
    Go to OpenAI documentation -> View API keys -> Create new secret key -> Add it to .env file

## Generate Discord token
    Go to Discord Developer Portal -> Applications -> New Applicaiton -> Enter App_name -> Create
    1. Go to Bot -> Add Bot
    2. Go to OAuth2 -> URL Generator -> Under scope option select 'bot'.
    3. Under 'Bot Permissions' select administrator and other permissions as per the requirement.
    4. Copy the Generated URL and save it somewhere safe.
    5. Go OAuth2 -> General -> Default AUTHORIZATION LINK
    6. Under Authorization method select 'Custom URL' from the menu and under CUSTOM URL paste the
       URL that we copied in Step-4 and save changes.
    7. Go to Bot and enable MESSAGE CONTENT INTENT and save changes.
    8. Go to Bot and click on RESET TOKEN (This is the API token). Save this somewhere safe.

## Adding Bot to a Server
    1. Paste the link into a browser and click enter.
    2. Add the bot to a server.
    3. Review and authorize the permissions.
    
## Snapshots
    
![Snapshot-Chatbot](https://user-images.githubusercontent.com/95921032/216701229-67b62697-47dd-429a-ac6f-697b7a2485b1.jpeg)
