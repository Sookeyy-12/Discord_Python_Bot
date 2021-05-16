import discord
from discord.ext import commands
import random
from cogs.packages.jokes import get_joke        # importing get_joke from packages
from cogs.packages.memes import get_meme        # importing get_meme from packages
from cogs.packages.quotes import get_quote      # importing get_quote from packages
import time

bot = commands.Bot(command_prefix="!")  # define bot

class BotCommands(commands.Cog):
    """ General Bot Commands """
    def __init__(self, bot):
        self.bot = bot

    # Hello command
    @commands.command()
    async def hello(self, ctx):
        """ Says Hello! """
        await ctx.channel.send("Hello! :wave:")

    # Cat
    @commands.command()
    async def cat(self, ctx):
        """ Ya like Cats? """
        await ctx.channel.send('ᓚᘏᗢᓓ ◯')

    # Joke Command
    @commands.command()
    async def joke(self, ctx):
        """ Generates a random Joke """
        joke = get_joke()
        await ctx.channel.send(joke)

    # Question Command
    @commands.command()
    async def q(self, ctx):
        """ Ask a Y/N Question. Usage: !q <your y/n question> """
        x = random.randint(0,1)     # for question command
        list1 = ['yes', 'no']
        await ctx.channel.send(list1[x])

    # Meme Command
    @commands.command()
    async def meme(self, ctx):
        """ Generates a Random meme from r/memes """
        meme = get_meme()
        await ctx.channel.send(meme)

    # Quote Command
    @commands.command()
    async def quote(self, ctx):
        """ Generates a Random Famous Quote """
        quote = get_quote()
        await ctx.channel.send(quote)

def setup(bot):
    bot.add_cog(BotCommands(bot))