import os
from discord.ext.commands import Bot

client = Bot(command_prefix="[]")
client.load_extension('cogs.role')


@client.event
async def on_ready():
    print("session started")


@client.command(name="ping", aliases=["ping", "pong"])
async def ping(ctx):
    await ctx.send(client.latency)


client.run(os.getenv('DISCORD_TOKEN'))