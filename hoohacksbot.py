##hoohacksbot.py
import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

classname = [] #holds the class name
urls = [] #holds the corresponding urls (name and data)
size = 0

assignment = []
deadline = []
s = 0

@client.event
async def on_message(text):
    if text.content.startswith('!help'):
        question = text.content[5:]
        textAuthor = text.author
        await text.delete()
        embed = discord.Embed(title = 'Help!', description= 'Help requested by ' + text.author.mention + \
        '\n React with a :white_check_mark: if your question has been resolved!'\
        '\n React with a :x: if you no longer need help', color=0xF84C1E)
        embed.add_field(name = "Question:" , value= question, inline=False)
        msg = await text.channel.send(embed=embed)
        reaction = await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        await msg.add_reaction("✅")
        
        def check(reaction, user):
            return user == textAuthor and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')
        reaction, user = await client.wait_for('reaction_add', check=check)
        await msg.delete()

    elif text.content.startswith('!info'):
        await text.delete()
        embed = discord.Embed(title = 'Info!', description= 'Use !help and add your question directly after to ask for help, in the format of !help "Question"' \
        , color=0xF84C1E)
        msg = await text.channel.send(embed=embed)

    '''

    elif text.content.startswith('!addclass'):
        #await text.delete()
        await text.send(f"y or n")
        def check(msg):
            return msg.author == text.author and msg.channel == text.channel and \
            msg.content.lower() in ["y", "n"]

        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == "y":
            await ctx.send("You said yes!")
        else:
            await ctx.send("You said no!")
        
        classname[size] = input("Enter your class name: ")
        url[size] = input("Enter your class link: ")
        size = size + 1 
        await text.channel.send("Class has been added") 

        
    
    elif text.content.startswith('!adddeadlines'):
        await text.delete()
        assignment[s] = input("Enter your assignment: ")
        deadline[s] = input("Enter your deadline: ")
        s = s + 1 
        await text.channel.send("Assignment has been added") 
        

    elif text.content.startswith('!geturls'):
        await text.delete()
        for x in range(size):  
            await text.channel.send(classname[i] + ' - ' + url[i]) #lists urls for zoom links
        
    
    elif text.content.startswith('!getdeadlines'):
        await text.delete()
        await text.delete()
        for x in range(s): 
            await text.channel.send(assignment[i] + ' due ' + deadline[i]) #lists deadlines for assignments   

'''     
        

client.run(TOKEN)






