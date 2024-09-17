import os
import discord
from discord.ext import tasks
from datetime import datetime
from dotenv import dotenv_values


config = dotenv_values(".env")

TOKEN = config['DISCORD_BOT_TOKEN']
CHANNEL_ID = config['DISCORD_CHANNEL_ID']

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    send_weekly_message.start() # Start the daily check loop
    
# check every day at a set interval (24 hours)    
@tasks.loop(hours = 24)
async def send_weekly_message():
    # Get the current dat of the week ( 0 = Monday, 6 = Sunday)
    current_day = datetime.now().weekday()
    current_hour = datetime.now().hour # Get the current hour (0 - 23)
    current_minute = datetime.now().minute
    
    # Check if it's a Monday (0) or Thursday (3) and if it's 9AM
    if (current_day == 0) and current_hour == 9:
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.send(f"@Channel what is everyone's availability this Saturday for our match? please react to this message with ✅ , ❓ , ❌")
    
        # Add reactions to the message
        await message.add_reaction("✅")
        await message.add_reaction("❓")
        await message.add_reaction("❌")
        
    elif (current_day == 3) and current_hour == 9:
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.send(f"@Channel what is everyone's availability Thursday practice session? please react to this message with ✅ , ❓ , ❌")
    
        # Add reactions to the message
        await message.add_reaction("✅")
        await message.add_reaction("❓")
        await message.add_reaction("❌")
    else:
        print(f"No message sent today at {current_hour}{current_minute} on day {current_day}.")

# Run the bot
client.run(TOKEN)