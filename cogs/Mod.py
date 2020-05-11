import discord
from discord.ext import commands
import typing


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def how_to_purge(ctx, amount: int, check=None):
        try:
            p = await ctx.channel.purge(limit=amount, check=check)
            return len(p)
        except discord.Forbidden:
            try:
                p = await ctx.channel.purge(limit=amount, check=check, bulk=False)
                return len(p)
            except:
                d = 0
                async for message in ctx.channel.history(limit=limit):
                    if check is not None:
                        if check:
                            await message.delete()
                            d += 1
                return d

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, user: typing.Optional[discord.User], amount: int = 50):
        """Purge messages"""
        if ctx.invoked_subcommand is not None:
            return
        check = None
        if user is not None:
            def check(m):
                return m.author.id == user.id
        await ctx.message.delete()
        m = await self.how_to_purge(ctx, amount, check=check)
        await ctx.send(f"Removed {m} messages.", delete_after=5)
        ml = discord.Embed(title="Messages purged", description="**Mod:** {} (`{}`)\n**Amount:** {}".format(ctx.message.author.mention, str(ctx.author), m))
        channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
        await channel.send(embed=ml)
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason='No reason'):
        if member.top_role <= ctx.author.top_role:
            await ctx.send("`{}` was warned successfully".format(str(member)))
            ml = discord.Embed(title="User warned", description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(member.mention, str(member), ctx.message.author.mention, str(ctx.author), reason))
            channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
            await channel.send(embed=ml)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason='No reason'):
        if member.top_role <= ctx.author.top_role:
            await member.ban(reason=reason)
            await ctx.send("`{}` was banned from the server.".format(str(member)))
            ml = discord.Embed(title="User banned",
                            description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(member.mention, str(member), ctx.message.author.mention, str(ctx.author), reason))
            channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
            await channel.send(embed=ml)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, *, reason='No reason'):
        await ctx.guild.unban(user, reason=reason)
        await ctx.send("{} was successfully unbanned.".format(user.mention))
        ml = discord.Embed(title="User unbanned",
                           description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(user.mention, str(user), ctx.message.author.mention, str(ctx.author), reason))
        channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
        await channel.send(embed=ml)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason='No reason'):
        if member.top_role <= ctx.author.top_role:
            await member.kick(reason=reason)
            await ctx.send("`{}` was kicked from the server.".format(str(member)))
            ml = discord.Embed(title="User kicked",
                                description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(member.mention, str(member), ctx.message.author.mention, str(ctx.author), reason))
            channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
            await channel.send(embed=ml)

    @commands.command()
    @commands.bot_has_permissions(manage_guild=True)
    @commands.has_permissions(manage_guild=True)
    async def mute(self, ctx, member: discord.Member, *, reason='No reason'):
        if member.top_role <= ctx.author.top_role:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.add_roles(role)
            await ctx.send("`{}` was muted.".format(str(member)))
            ml = discord.Embed(title="User muted",
                               description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(member.mention, str(member), ctx.message.author.mention, str(ctx.author), reason))
            channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
            await channel.send(embed=ml)

    @commands.command()
    @commands.bot_has_permissions(manage_guild=True)
    @commands.has_permissions(manage_guild=True)
    async def unmute(self, ctx, member: discord.Member, *, reason='No reason'):
        if member.top_role <= ctx.author.top_role:
            role = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(role)
            await ctx.send("`{}` was successfully unmuted.".format(str(member)))
            ml = discord.Embed(title="User unmuted",
                               description="**User:** {} (`{}`)\n**Mod:** {} (`{}`)\n**Reason:** {}".format(member.mention, str(member), ctx.message.author.mention, str(ctx.author), reason))
            channel = discord.utils.get(ctx.message.guild.text_channels, name='mod-logs')
            await channel.send(embed=ml)


def setup(bot):
    bot.add_cog(Mod(bot))
