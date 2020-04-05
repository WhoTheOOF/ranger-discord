import discord
from discord.ext import commands
import time
import datetime
import traceback
import typing
import random
import asyncio
from jishaku import help_command
t =  datetime.datetime.today()
dt = t.strftime('%a, %d, %B, %Y, %I:%M %p')

start = time.time()
bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('r-'), description=None, max_messages=9999,
                              case_insensitive=True, activity=discord.Game(name="Loading..."),
                              status=discord.Status.do_not_disturb, help_command=help_command.MinimalEmbedPaginatorHelp())


toload = ["cogs.Main"]
bot.cogss = toload
bot.boot_time = 0
bot.loadedcogs = 0


@bot.event
async def on_ready():
    success = 0
    for c in toload:
        try:
            bot.load_extension(c)
            bot.loadedcogs += 1
            success += 1
        except:
            pass
    print("__________________________________________")
    print("Logged in as: {}".format(bot.user.name))
    print("Total guilds: {}".format(len(bot.guilds)))
    print("Total users : {}".format(len(bot.users)))
    purged = 0
    for g in bot.guilds:
        for c in g.channels:
            if c.name == 'p-auto-purge':
                try:
                    d = await c.purge(limit=9999999, bulk=True)
                    purged += len(d)
                except Exception as e:
                    await g.owner.send(f"I was unable to purge messages in your 'p-auto-purge' (<#{c.id}>) channel"
                                       f" for the following error:\n{e}")
    print(f"Successfully cleared {purged} backlogged messages.")
    done = time.time()
    bt = round(done - start)
    bot.boot_time += bt
    print("Boot time   : {}s".format(bt))
    print("Total loaded: {}".format(success))
    print("__________________________________________")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="r-help | v1.0"))
    bot.load_extension('guildmanager.cog')
    _ = bot.get_channel(655451873918320650)
    ctx = await bot.get_context(await _.fetch_message(692489954793750538))
    ctx.command = bot.get_command('jsk embedhelp')
    

    
bot.owner_ids = [
          533520461653606410
]

bot.load_extension('jishaku')

@bot.command(aliases=['reload'], hidden=True)
@commands.is_owner()
async def r(ctx, cog: str):
    try:
        if cog == 'all':
            successful = ""
            for c in toload:
                try:
                    try:
                        bot.reload_extension(c)
                    except commands.ExtensionNotLoaded:
                        bot.load_extension(c)
                    successful += ":repeat: - Reloaded `{}`\n".format(c)
                except:
                    print(f'{traceback.format_exc()}__________________________________________')
                    successful += ":warning: - Failed to reload `{}`\n".format(c)
                    continue
            await ctx.send(successful)
        else:
            try:
                bot.reload_extension(cog)
            except commands.ExtensionNotLoaded:
                bot.load_extension(cog)
            await ctx.send(":repeat: - Reloaded `{}`\n".format(cog), delete_after=10)
    except Exception as e:
        print(f'{traceback.format_exc()}__________________________________________')
        await ctx.send(f'```py\n{e}\n```Full error in console')

with open('token.txt', 'r') as tokens: # THE S ON THIS LINE
  bot.tokens = [line.strip() for line in tokens.readlines()]

bot.run(bot.tokens[0])
