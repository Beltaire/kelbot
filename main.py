import os
import discord
from discord.ext import commands

TOKEN = "OTIzNjM5ODI0MzM2OTc3OTQy.YcS8ng.nJsrKpWQgI1l61FH4M2vIPinogI"
extensions = ["KelCommands"]
bot = commands.Bot(command_prefix="$")
class startup(discord.Client):
    @bot.event
    async def on_ready():
        print("Logged on as {0}!".format(bot.user))
    @bot.event
    async def on_message(message):
        print("Message from {0.author}: {0.content}".format(message))
        await bot.process_commands(message)
if __name__ == "__main__":
    for i in extensions:
        bot.load_extension(i)
bot.run(TOKEN)
