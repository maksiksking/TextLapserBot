import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="messages burning"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author == "720351927581278219":
        return

    if "gif" not in message.channel.name:
        if "leader" not in message.channel.name:
            return
        else:
            if "/leaderboard" not in message.content:
                await message.delete()
                await message.channel.send("Only **/leaderboard** command is allowed here", delete_after=5)
    else:
        if "gif" and "http" and "tenor" not in message.content:
            await message.delete()
            await message.channel.send("Only GIF's are allowed", delete_after=5)


client.run() # your api token
# yup
