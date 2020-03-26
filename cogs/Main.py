import discord
from discord.ext import commands
import datetime
import random
import asyncio

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, user: discord.User):
        """Grab an avatar from any user in the server"""
        embed = discord.Embed()
        user = user or ctx.author
        avatar = user.avatar_url_as(static_format='png')
        embed.set_author(name=str(user), url=avatar)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    @commands.command()
    async def testembed(self, ctx):
        embed = discord.Embed(title="Title", description="Description", colour=discord.Color.blue(), url="https://www.google.com")

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_image(url="https://discordpy.readthedocs.io/en/rewrite/_images/snake.png")
        embed.set_thumbnail(url="https://www.python.org/static/img/python-logo.png")

        embed.add_field(name="Field 1", value="Value 1")
        embed.add_field(name="Field 2", value="Value 2")
    
        embed.add_field(name="Field 3", value="Value 3", inline=False)
        embed.add_field(name="Field 4", value="Value 4")

        await ctx.send(embed=embed)
        
    @commands.command()
    async def ping(self, ctx):
        """Get the bot's ping"""
        embed = discord.Embed(description=":ping_pong: **Pong!**\nPing: {0}ms".format((round(ctx.bot.latency * 1000))), color=0x36393E)
        await ctx.send(embed=embed)
        
    @commands.command(aliases=['binfo', 'about', 'stats'])
    async def info(self, ctx):
        embed = discord.Embed(title="", colour=0x36393E)
        embed.set_author(name="Bot Information",
                         icon_url="https://cdn.discordapp.com/avatars/692487204441817200/05d82251bc246225507ce639d4e79d1d.png?size=1024")
        embed.set_footer(text="Made with love by J_J#2112",
                         icon_url="https://cdn.discordapp.com/avatars/692487204441817200/05d82251bc246225507ce639d4e79d1d.png?size=1024")
        # embed.set_image(url="https://cdn.discordapp.com/avatars/554852324376313856/d1e157c1f5b8fa94ca18b66a7b8d4b91.png?size=256")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/692487204441817200/05d82251bc246225507ce639d4e79d1d.png?size=1024")

        embed.add_field(name="**Owner**", value="<@533520461653606410>", inline=True)
        embed.add_field(name="**Library**", value="discord.py", inline=True)
        embed.add_field(name="**Server Count**", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="**Bot Users**", value=len(self.bot.users), inline=True)
        embed.add_field(name="**Support Server**", value="https://discord.gg/RPD67Db", inline=True)
        embed.add_field(name="**Source Code**", value="[Click me](https://github.com/WhoTheOOF/ranger-discord)", inline=True)
        
        await ctx.send(embed=embed)
        
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(description="[Bot Invite](https://discordapp.com/oauth2/authorize?client_id=692487204441817200&scope=bot)\n\n[Support Server](https://discord.gg/RPD67Db)\n\n[Source Code](https://github.com/WhoTheOOF/ranger-discord)")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def source(self, ctx):
        embed = discord.Embed(description="[Source Code](https://github.com/WhoTheOOF/ranger-discord)")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Main(bot))
