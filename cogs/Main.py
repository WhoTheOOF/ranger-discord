import discord
from discord.ext import commands
import datetime
import os
import inspect
import random
import asyncio
from psutil import Process
from os import getpid

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def gay(self, ctx, user: discord.User = None):
        """tell how game someone is, k boomer"""
        user = user if user is not None else ctx.author
        input = len(user.name)
        middle = input / 5
        end = (middle * 60) / 3
        output = end - 0.3
        if round(output) > 100:
            output = 100
        await ctx.send(f'**{user.name}** is **{output}%** gay!')
        
    @commands.command(name='source', aliases=['getcode', 'gcode', 'getc', 'sourcecode', 'scode', 'sourcec'])
    async def _source(self, ctx, *, command: str = None):
        """Displays my full source code or for a specific command."""
        source_url = "https://github.com/WhoTheOOF/ranger-discord"
        branch = "master"
        if command is None:
            return await ctx.send(f"support my dev by uh, giving a star on github; !\n{source_url}")

        if command == "help":
            src = type(self.bot.help_command)
            module = src.__module__
            filename = inspect.getsourcefile(src)
        else:
            obj = self.bot.get_command(command.replace(".", " "))
            if obj is None:
                return await ctx.send("Could not find command.")

            # since we found the command we're looking for, presumably anyway, let's
            # try to access the code itself
            src = obj.callback.__code__
            module = obj.callback.__module__
            filename = src.co_filename

        lines, firstlineno = inspect.getsourcelines(src)
        if module.startswith("jishaku"):
            location = module.replace(".", "/") + ".py"
            source_url = "https://github.com/Gorialis/jishaku"
            branch = "master"
            final_url = f"<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>"
            return await ctx.send(final_url)
        if not module.startswith("discord"):
            # not a built-in command
            location = os.path.relpath(filename).replace("\\", "/")
        else:
            location = module.replace(".", "/") + ".py"
            source_url = "https://github.com/Rapptz/discord.py"
            branch = "master"

        final_url = f"<{source_url}/blob/{branch}/{location}#L{firstlineno}-L{firstlineno + len(lines) - 1}>"
        await ctx.send(final_url)
        
    @commands.command(aliases=['mem', 'm'], hidden=True)
    @commands.is_owner()
    async def memory(self, ctx):
        await ctx.send(f'Ranger is currently using **{round(Process(getpid()).memory_info().rss/1024/1024, 2)} MB** of memory.')

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

        embed.add_field(name="**Owner**", value="<@699751199850758267>", inline=True)
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
        
def setup(bot):
    bot.add_cog(Main(bot))
