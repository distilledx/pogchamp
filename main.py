import discord
from discord.ext import commands
from uwu.main import uwuify
import requests
import shitpost
from peko.main import pekify
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


intents = discord.Intents.all()
intents.typing = False

bot = commands.Bot(command_prefix=',', intents=intents,
                   help_command=None, case_insensitive=True)
bot.solving = False
server = 0

bot.deleted_messages = {}
bot.zwnjs = {}
bot.edited_messages = {}


@bot.event
async def on_user_update(before, after):
    if before.avatar_url == after.avatar_url:
        return

    if after.id != 808386830600110172:
        return

    data = requests.get(after.avatar_url)
    await bot.user.edit(avatar=data.content)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound) or isinstance(error, commands.MissingRequiredArgument):
        return
    raise error


def isnewint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


async def better_on_ready():
    await bot.wait_until_ready()
    print('oh yeah')
    bot.mainserver = bot.get_guild(796060146048041020)
    bot.bruh = await bot.mainserver.fetch_emoji(872006627732123648)
    bot.ducky = await bot.mainserver.fetch_emoji(832245856342245376)
    bot.oof = await bot.mainserver.fetch_emoji(832543178670080061)
    bot.thrinking = await bot.mainserver.fetch_emoji(819140786066292740)
    bot.owo = await bot.mainserver.fetch_emoji(832808383500910592)
    bot.pantsu = await bot.mainserver.fetch_emoji(832808386025357342)
    bot.amogus = await bot.mainserver.fetch_emoji(877810541886861322)
    bot.ayaya = await bot.mainserver.fetch_emoji(888029604026150972)
    bot.mainchannel = bot.mainserver.get_channel(796060146048041023)


@bot.event
async def on_message(message):
    if (message.author.id == 722783336485093389) and not (message.content.startswith(',')):
        msg = await message.channel.fetch_message(message.id)
        await msg.delete()
        yours = uwuify(message.content + '\n')
        yours = yours.replace('  ', ' ')
        yours = yours.replace('   ', ' ')

        attachments = ' '
        if message.attachments:
            attachments = [i.proxy_url for i in message.attachments]
            attachments = '\n'.join(attachments)

        if message.reference != None:
            reply_to = await message.channel.fetch_message(message.reference.message_id)
            await message.channel.send(content=f'{yours} \n {attachments}', reference=reply_to)
        else:
            await message.channel.send(content=f'{yours} \n {attachments}')

    try:

        for i in ('pog', 'but', 'oof', 'hmm', 'owo', 'weuew', 'welp', 'bruh', 'sus', 'ayaya'):
            if i not in message.content.lower():
                if 'pog' in message.content.lower():
                    await message.add_reaction(bot.ducky)

                if 'but' in message.content.lower():
                    await message.add_reaction('🍑')

                if 'oof' in message.content.lower():
                    await message.add_reaction(bot.oof)

                if 'hmm' in message.content.lower():
                    await message.add_reaction(bot.thrinking)

                if 'owo' in message.content.lower():
                    await message.add_reaction(bot.owo)

                if 'weuew' in message.content.lower():
                    await message.add_reaction(bot.pantsu)

                if 'welp' in message.content.lower():
                    await message.add_reaction('💀')

                if 'bruh' in message.content.lower():
                    await message.add_reaction(bot.bruh)

                if 'sus' in message.content.lower():
                    await message.add_reaction(bot.amogus)

                if 'ayaya' in message.content.lower():
                    await message.add_reaction(bot.ayaya)
                break
    except:
        pass

    await bot.process_commands(message)


@bot.event
async def on_raw_message_delete(message):
    try:
        if bot.deleted_messages[message.guild_id]:
            pass
    except:
        bot.deleted_messages[message.guild_id] = []

    if len(bot.deleted_messages[message.guild_id]) < 10:
        try:
            if '‌' not in message.cached_message.content:
                bot.deleted_messages[message.guild_id].append(
                    message.cached_message)
            else:
                if message.author.display_name not in bot.zwnjs:
                    pass
        except:
            return
    else:
        try:
            if '‌' not in message.cached_message.content:
                del bot.deleted_messages[message.guild_id][0]
                bot.deleted_messages[message.guild_id].append(
                    message.cached_message)
        except:
            return


@bot.event
async def on_raw_message_edit(message):
    try:
        if bot.edited_messages[message.guild_id]:
            pass
    except:
        bot.edited_messages[message.guild_id] = []

    if len(bot.edited_messages[message.guild_id]) < 10:
        try:
            bot.edited_messages[message.guild_id].append(
                message.cached_message)
        except:
            return
    else:
        try:
            del bot.edited_messages[message.guild_id][0]
            bot.edited_messages[message.guild_id].append(
                message.cached_message)
        except:
            return


@bot.command(name='echo')
async def echo(ctx, *args):
    if ctx.author.id == 434747706649346059:
        await bot.mainchannel.send(' '.join(args))


@bot.command(name="run")
async def run(ctx):
    if ctx.author.id == 434747706649346059:
        a = ctx.message.content
        b = a[5::].lstrip('```py').rstrip('```')
        await func_parse(b)


async def func_parse(a):
    if 'await' not in a:
        return exec(a, globals())
    else:
        exec(f'async def __ex():' +
             ''.join(f'\n   {l}' for l in a.split('\n')), globals(), locals())
        return await locals()['__ex']()


@bot.command(name='blip')
async def blip(ctx):
    await ctx.send('boop')


@bot.command(name='meirl')
async def meirl(ctx):
    await ctx.send('don\'t look at me im totally not having transgender feelings')


@bot.command(name='test')
async def test(ctx):
    await ctx.send('E er')


@bot.command(name='random')
async def random(ctx):
    await ctx.send(f'> {shitpost.send()}')


@bot.command(name='purge', aliases=['p'])
async def delt(ctx, number):
    if ctx.author.id in (722783336485093389, 698386832370696233, 434747706649346059):
        number = int(number) + 1
        deleted = await ctx.channel.purge(limit=number, check=None)
        await ctx.channel.send(f'Deleted {len(deleted) - 1} message(s)', delete_after=1)


@bot.command(name='pic')
async def pic(ctx, member: discord.Member):
    pic = member.avatar_url
    await ctx.send(f'{pic}')


@bot.command(name='snipe', aliases=['s'])
async def snipe(ctx, *args):
    try:
        if bot.deleted_messages[ctx.guild.id]:
            pass
    except:
        await ctx.send('u haven\'t deleted anything yet :eyes: scawy')
        return

    if len(bot.deleted_messages[ctx.guild.id]) == 0:
        await ctx.send('u haven\'t deleted anything yet :eyes: scawy')
        return
    if len(args) == 0:
        if bot.deleted_messages[ctx.guild.id][-1] == None:
            await ctx.send('looks like that message wasn\'t cached. Good chance that it was sent before the bot started')
            return
        if len(bot.deleted_messages[ctx.guild.id]) == 0:
            await ctx.send('doesn\'t look like i stored that many messages')
            return
        to_send = bot.deleted_messages[ctx.guild.id][-1]
        embed = discord.Embed(title=str(to_send.author),
                              description=str(to_send.content), color=0x8000DE)
        if to_send.attachments:
            for i in to_send.attachments:
                if i.content_type.startswith('image'):
                    embed.set_image(url=i.proxy_url)
                    break
        embed.timestamp = to_send.created_at
        embed.set_footer(text=f'Delete snipe requested by {ctx.author.name}')
        try:
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed)
        return
    if len(args) > 1:
        await ctx.send('can get only 1 message at a time')
        return
    if isnewint(args[0]) == False:
        await ctx.send('argument has to be an INTEGER')
        return
    if (int(args[0]) < -9) or (int(args[0]) > 10):
        await ctx.send('argument has to be between -9 and 10')
        return
    if int(args[0]) > len(bot.deleted_messages[ctx.guild.id]):
        await ctx.send('doesn\'t look like i stored that many messages')
        return
    to_send = bot.deleted_messages[ctx.guild.id][-1*int(args[0])]
    if to_send == None:
        await ctx.send('looks like that message wasn\'t cached. Good chance that it was sent before the bot started')
        return
    embed = discord.Embed(title=str(to_send.author),
                          description=str(to_send.content), color=0x8000DE)
    embed.timestamp = to_send.created_at
    if to_send.attachments:
        for i in to_send.attachments:
            if i.content_type.startswith('image'):
                embed.set_image(url=i.proxy_url)
                break
    embed.set_footer(text=f'Delete snipe requested by {ctx.author.name}')
    try:
        await ctx.reply(embed=embed)
    except:
        await ctx.send(embed=embed)


@bot.command(name='editsnipe', aliases=['es'])
async def edit_snipe(ctx, *args):
    try:
        if bot.edited_messages[ctx.guild.id]:
            pass
    except:
        await ctx.send('u haven\'t edited anything yet :eyes: scawy')
        return

    if len(bot.edited_messages[ctx.guild.id]) == 0:
        await ctx.send('u haven\'t edited anything yet :eyes: scawy')
        return
    if len(args) == 0:
        if bot.edited_messages[ctx.guild.id][-1] == None:
            await ctx.send('looks like that message wasn\'t cached. Good chance that it was sent before the bot started')
            return
        if len(bot.edited_messages[ctx.guild.id]) == 0:
            await ctx.send('doesn\'t look like i stored that many messages')
            return
        to_send = bot.edited_messages[ctx.guild.id][-1]
        embed = discord.Embed(title=str(
            to_send.author), description=f'{to_send.content}\n[Click here owo]({to_send.jump_url} \"nyaa~\")', color=0x8000DE)
        embed.timestamp = to_send.created_at
        embed.set_footer(text=f'Edit snipe requested by {ctx.author.name}')
        try:
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed)
        return
    if len(args) > 1:
        await ctx.send('can get only 1 message at a time')
        return
    if isnewint(args[0]) == False:
        await ctx.send('argument has to be an INTEGER')
        return
    if (int(args[0]) < -9) or (int(args[0]) > 10):
        await ctx.send('argument has to be between -9 and 10')
        return
    if int(args[0]) > len(bot.edited_messages[ctx.guild.id]):
        await ctx.send('doesn\'t look like i stored that many messages')
        return
    to_send = bot.edited_messages[ctx.guild.id][-1*int(args[0])]
    if to_send == None:
        await ctx.send('looks like that message wasn\'t cached. Good chance that it was sent before the bot started')
        return
    embed = discord.Embed(title=str(
        to_send.author), description=f'{to_send.content}\n[Click here owo]({to_send.jump_url} \"nyaa~\")', color=0x8000DE)
    embed.timestamp = to_send.created_at
    embed.set_footer(text=f'Edit snipe requested by {ctx.author.name}')
    try:
        await ctx.reply(embed=embed)
    except:
        await ctx.send(embed=embed)


@bot.command(name='wipe', aliases=['w'])
async def wipe(ctx, name):
    if ctx.author.id in (434747706649346059, 698386832370696233):
        if name == 'snipe':
            del bot.deleted_messages[ctx.guild.id]
            await ctx.reply('Deleted snipe list <:thumbsup:819461171496091670>')
        elif name == 'editsnipe':
            del bot.edited_messages[ctx.guild.id]
            await ctx.reply('Deleted edit list <:thumbsup:819461171496091670>')


@bot.command(name='uwu')
async def func_uwu(ctx, *, string):
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(uwuify(string).replace('`', r'\`')[0:2000])


@bot.command(name='peko')
async def func_pek(ctx, *, string):
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(pekify(string)[0:2000])


@bot.command(name='update')
async def update(ctx, channel: discord.TextChannel, *, string):
    owner = (await bot.application_info()).owner
    if ctx.author != owner:
        return
    updates = '\n'.join(string.split(';;'))
    embed = discord.Embed(title='UPDATES', description=updates, color=0x8000DE)
    await channel.send(embed=embed)

bot.loop.create_task(better_on_ready())
bot.run(TOKEN)
