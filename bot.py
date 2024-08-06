import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def createtopic(ctx, *, topic: str):
    guild = ctx.guild
    existing_role = discord.utils.get(guild.roles, name=topic)
    if existing_role:
        await ctx.send(f'The role "{topic}" already exists.')
    else:
        new_role = await guild.create_role(name=topic)
        await ctx.send(f'Role "{topic}" has been created.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!topic'):
        topic = message.content[len('!topic '):]
        guild = message.guild
        existing_role = discord.utils.get(guild.roles, name=topic)
        if not existing_role:
            new_role = await guild.create_role(name=topic)
            await message.channel.send(f'Role "{topic}" has been created.')

    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
