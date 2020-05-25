import discord
from discord.ext import commands

class Events(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


  @commands.Cog.listener()
  async def on_member_join(self, member):

    guild = member.guild
    channel = self.bot.get_channel(648009478750601227)

    if guild.id == 647996543999148067:

      await channel.send(f"<a:blobhi:696885698766307421> {member.mention} ({member}) has joined the server!")

  @commands.Cog.listener()
  async def on_member_remove(self, member):

    guild = member.guild
    channel = self.bot.get_channel(648009478750601227)

    if guild.id == 647996543999148067:

      await channel.send(f"<a:blobhi:696885698766307421> {member.mention} ({member}) has left the server.")
      
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    embed = discord.Embed(description="<a:blobhi:696885698766307421> **Joined a server**\n\n**Name:** {}\n\n**ID:** {}\n\n**Owner:** {} (`{}`)".format(guild.name, guild.id, guild.owner.mention, guild.owner.id))
    await self.bot.get_channel(648010351186673664).send(embed=embed)
    
  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    embed = discord.Embed(description="<a:blobhi:696885698766307421> **Left a server**\n\n**Name:** {}\n\n**ID:** {}\n\n**Owner:** {} (`{}`)".format(guild.name, guild.id, guild.owner.mention, guild.owner.id))
    await self.bot.get_channel(648010351186673664).send(embed=embed)
    
  @commands.Cog.listener()
  async def on_member_join(self, member):

    guild = member.guild
    channel = self.bot.get_channel(702357773924696144)

    if guild.id == 702355649237090424:

      await channel.send(f"<a:blobhi:696885698766307421> {member.mention} ({member}) has joined **JumpKits**!")

  @commands.Cog.listener()
  async def on_member_remove(self, member):

    guild = member.guild
    channel = self.bot.get_channel(702357773924696144)

    if guild.id == 702355649237090424:

      await channel.send(f"<a:blobhi:696885698766307421> {member.mention} ({member}) has left **JumpKits**.")
      
def setup(bot):
  bot.add_cog(Events(bot))
