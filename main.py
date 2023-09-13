import discord
import os

TOKEN = "enter your bot code here"
RESULT_CHANNEL_ID = 863271725947813928
PING_ROLE_ID = 775568100472651817


f = open("log.txt", 'a')
client = discord.Client()

#written by thegreat12#1886
#customised for itsu 
#v2- fixed the bug where there would be a ping but no message if a file was uploaded


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('?apply'):
        us = message.author
        u = str(us)
        c = 'Hello ' + u[:-5:] + ' !!'

        await us.send(f'{c}\n')

        #await message.channel.send(c)

        def verify(m):
            return m.author != client.user

        await us.send('Starting Application \n')

        questions = ['Discord ID:',
            'Do you follow itsuartistry on instagram?:',
            'How active are you in chat (1-5):', 'Instagram name:',
            'Edit link:', 'Why do you want to join itsu?:',
            'Any questions or remarks?:'
        ]
        answers = []

        answers.append(us)
        i = 1
        while i < len(questions):
            await us.send(questions[i])

            a = await client.wait_for('message', check=verify)
            if a.content == '':
                await us.send(
                    "Invalid input type. Do not upload any file. Answer the question again please."
                )
            else:
                answers.append(a.content)
                i += 1

        def final(m):
            global send
            send = True
            if m.author != client.user and m.content not in ['y', 'Y']:
                send = False

            return (m.author != client.user)

        await us.send('Do you want to submit it (Y/N)? ')
        await client.wait_for('message', check=final)

        if send:
            await us.send("Thanks for applying. ")

            channel = client.get_channel(RESULT_CHANNEL_ID)
           
            emb = discord.Embed(title='New application',
                                description="",
                                color=0x00ff00)
            for i in range(0, len(questions)):
                emb.add_field(name=f'{questions[i]}',
                              value=f'{answers[i]}',
                              inline=False)
            await channel.send(f'<@&{PING_ROLE_ID}>')
            await channel.send(embed=emb)
        else:
            await us.send("Cancelled application.")

    if message.content.startswith('!test'):
        embedVar = discord.Embed(title="Title",
                                 description="Desc",
                                 color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)


@client.event
async def on_disconnect():
    print('{0.user} has disconnected/logged out'.format(client))


@client.event
async def on_reconnect():
    print('We have relogged in as {0.user}'.format(client))


client.run(TOKEN)
