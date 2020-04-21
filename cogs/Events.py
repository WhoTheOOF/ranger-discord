import discord
import utils
from discord.ext import commands
from utils import objects

class Events(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


    def has_permission(self, guild):
        return guild.me.guild_permissions.view_audit_log

    async def get_audit_logs(self, guild, limit=100, user=None, action=None)->list:
        try:
            return await self.bot.get_guild(guild.id).audit_logs(limit=limit, user=user, action=action).flatten()
        except:
            return []

    def get_embed(self, color=0xFFFF00):
        emb = commands.Embed()
        emb.colour = color
        emb.timestamp = datetime.datetime.utcnow()
        return emb

    def get_state(self, guild)->objects.LoggingFlags:
        if guild.id not in self.states:
            return None


        if self.states[guild.id] is not None and not self.states[guild.id].channel:
            return None

        return self.states[guild.id]

    async def send_to_channel(self, state, content=None, embed=None):
        channel = self.bot.get_channel(state.channel)
        if channel is None:
            return

        try:
            await channel.send(content, embed=embed)
        except commands.HTTPException:
            pass

  @commands.Cog.listener()
  async def on_member_ban(self, guild, user):
    state = self.get_state(guild)
    if state is None:
      return

    if not state.member_ban:
      return

    embed = self.get_embed(color=commands.Color.red())
    embed.title = "Ranger Logging - User Banned"
    embed.description = f"<:bancreate:702244371365363712> {user}\n"
    embed.set_footer(text=f"User ID: {user.id}")

    if not self.has_permission(guild):
      embed.description += "(I don't have permission to view audit logs, please give me permission)"
      await self.send_to_channel(state, embed=embed)
      return

    log = await self.get_audit_logs(guild, limit=1, action=discord.AuditLogAction.ban)
    log = log[0]
    embed.add_field(name="Moderator", value=f"{log.user.mention} - {log.user} (id: {log.user.id})")
    await self.send_to_channel(state, embed=embed)

  @commands.Cog.listener()
  async def on_member_unban(self, guild, user):
    state = self.get_state(guild)
    if state is None:
      return

    if not state.member_unban:
      return

    embed = self.get_embed(color=commands.Color.red())
    embed.title = "Ranger Logging - User Unbanned"
    embed.description = f"<:banremove:702244359390625862> {user}\n"
    embed.set_footer(text=f"User ID: {user.id}")

    if not self.has_permission(guild):
      embed.description += "(I don't have permission to view audit logs, please give me permission)"
      await self.send_to_channel(state, embed=embed)
      return

    log = await self.get_audit_logs(guild, limit=1, action=discord.AuditLogAction.unban)
    log = log[0]
    embed.add_field(name="Moderator", value=f"{log.user.mention} - {log.user} (id: {log.user.id})")
    await self.send_to_channel(state, embed=embed)
  
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
      
def setup(bot):
  bot.add_cog(Events(bot))
