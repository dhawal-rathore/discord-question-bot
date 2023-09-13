# discord-question-bot
Discord bot to ask questions to a specific user, and posts answers with questions in an embed into another channel
Uses the discord bot API to interactively acquire responses from users and returns an embed with readable answers 
into a specific channel and can also alert all people with a role if there is an application left to judge.

You will also need to change channels in the code for it to be applicable to your server,
questions can be changed in the code. 

# To Start



## Create your own bot account

You can create your own bot by creating a bot account for discord by creating a new application page
https://discordpy.readthedocs.io/en/stable/discord.html

Use the bot account token and insert it into TOKEN.

## Get Channel ID

This is where the results of the questions given to the users are sent. You can find it by right clicking on the channel and copying channel id. Paste into RESULT_CHANNEL_ID

## Get Role ID

This is where the users are pinged when there is a new answer. You can find it by right clicking on the role and copying role id. Paste into PING_ROLE_ID

## Add Bot to Server

Go to the application page you created and add it to your server.

# Using the bot

Run main.py on an computer connected to the internet. If terminal prints

We have logged in as ...

The bot is online.
