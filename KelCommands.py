from utils import tablecommands
from discord.ext import commands
import discord
import random
import re
import sqlite3

#This file will store the commands used by Kel,
#including internal commands and commands that may be
#used by the user.


class KelCommands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    
    @commands.command()
    async def createchar(self,ctx):
        await ctx.send("I can do that! Just give me the characters' name, class, level, max health, and stats!")
        response = await self.bot.wait_for("message",check=lambda m:m.author==ctx.author and m.channel==ctx.channel)
        msgsplit=re.split("[,()\s]",response.content)
        username=ctx.message.author.name
        charname = msgsplit[0]
        charclass = msgsplit[2]
        charlevel = msgsplit[4]
        charhealth = msgsplit[6]
        stre = msgsplit[9]
        dex = msgsplit[11]
        con=msgsplit[13]
        int=msgsplit[15]
        wis=msgsplit[17]
        cha=msgsplit[19]
        await ctx.send("Alright, you got it! Saving your character...")
        tablecommands.tableinsert(username,charname,charclass,charlevel,charhealth,stre,dex,con,int,wis,cha)
        await ctx.send("Character saved!")
        
    
    @commands.command()
    async def deletechar(self,ctx):
       await ctx.send("What a shame! Which character would you like to delete?")
       response = await self.bot.wait_for("message",check=lambda m:m.author==ctx.author and m.channel==ctx.channel)
       charname=response.content
       check=tablecommands.searchbychar(charname)
       print(check)
       if check is None:
           await ctx.send("I can't seem to find {}. Did you make any typos?".format(charname))
       else:
           await ctx.send("Alright I'll get to work!")
           await ctx.send("Deleting {}...".format(charname))
           tablecommands.deletechar(charname)
           await ctx.send("{} was deleted. We'll never forget you {}!".format(charname,charname))

    @commands.command()
    async def charinfo(self,ctx):
        await ctx.send("Which character do you wanna know about?")
        response = await self.bot.wait_for("message",check=lambda m:m.author==ctx.author and m.channel==ctx.channel)
        return
        
    @commands.command()
    async def roll(self,ctx):
            numrolled=0
            msgsplit = re.split(" |d",ctx.message.content)
            numofdice=int(msgsplit[1])
            dice=int(msgsplit[2])
            displaystring=""
            holderstring=""
            await ctx.send("Alright, you got it!")
            if numofdice!=1:
                for i in range(0,numofdice):
                    print(i)
                    randnum=random.sample(range(1,dice),1)
                    temp=("{}+".format(str(randnum[0])))
                    holderstring+=str(temp)
                    numrolled+=int(randnum[0])
                displaystring+=holderstring[:-1]
                temp=("={}".format(str(numrolled)))
                displaystring+=str(temp)
            else:
                randnum=random.sample(range(1,dice),1)
                temp1=("{}+".format(str(randnum[0])))
                holderstring+=str(temp1)
                
                numrolled+=int(randnum[0])
                displaystring+=holderstring[:-1]
                temp=("={}".format(str(numrolled)))
                displaystring+=str(temp)
            await ctx.send(displaystring)
    @commands.command()
    async def yo(self,ctx):
        await ctx.send("yo!".format(ctx))
def setup(bot):
    bot.add_cog(KelCommands(bot))