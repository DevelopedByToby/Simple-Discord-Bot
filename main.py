# I have no idea whether this bot still works, it is very old and developed really badly, I'm sorry!

# import discord (this line is essential if you want the bot to work, rmv the hashtag and note)

# import os (this line is not essential if non open source, if is open source, remove the hashtag at the beginning of this line and the note)

client = discord.Client()

@client.event
async def on_ready():
  print('Welcome back, you are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  if message.content.startswith ('!hello'):
      await message.channel.send ("Hello! I'm Chat Bot- but you can call me Talia! :)")

  if message.content.startswith ('!HelloBot'):
    await message.channel.send ('Hello friend! :D')

  if message.content.startswith ('!help'):
    await message.channel.send ('Hi there! I have been told that you need some help! :) Here are some commands you can use- !info !hello !bye !HelloBot !HowAreYou. Thank you! -Chat Bot')

  if message.content.startswith('!HowAreYou'):
    await message.channel.send ("Hey there! I am really good thanks- even though I'm a robot.  How are you? If you want to relpy you can use either good thanks or I'm bad")

  if message.content.startswith('good thanks'):
    await message.channel.send ("That's great!")

  if message.content.startswith ("I'm bad"):
    await message.channel.send ('Oh no! I hope you start feeling better soon!')

  if message.content.startswith ('!bye'):
      await message.channel.send ('Goodbye!')

  if message.content.startswith ('!info'):
      await message.channel.send ("This server is a discord Server! It's owner is -. Thank you. Oh and, I am a robot and you are a human! I hope you have an amazing day! :D")

  if message.content.startswith ('!WhatIsYourName'):
      await message.channel.send("My name is Talia! Nice to meet you! :D")

  if message.content.startswith('?!'):
      await message.channel.send("Yes... I'm here...!")

# token meant to go here, you do not need to worry abt hiding with os if done locally or non open source
