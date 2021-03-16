import os
import discord
from discord.ext.commands import Bot

client = Bot(command_prefix="[]")
client.load_extension('cogs.role')
client.remove_command('help')


@client.event
async def on_ready():
    print("session started")
    await client.change_presence(activity=discord.Game(name="Billy's Basement GameJam 2021"))


@client.command(name="ping", aliases=["pong"])
async def ping(ctx):
    await ctx.send(client.latency)


client.run(os.getenv('DISCORD_TOKEN'))
