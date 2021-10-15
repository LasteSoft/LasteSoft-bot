from discord.ext import commands
import os
import traceback
import discord
bot = commands.Bot(command_prefix='la!', help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    game = discord.Game(f"la! | {len(bot.guilds)}サーバー | {len(bot.users)}ユーザー")
    await bot.change_presence(activity=game, status=discord.Status.idle)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    channel = bot.get_channel(896321426175442964)#or896321426175442964
    await channel.send(error_msg)
    print(error_msg)
    await ctx.send(f'エラーが発生しました。\n**エラー内容**\n```{error_msg}```\n(開発者に送信しました)')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


token = os.getenv('DISCORD_BOT_TOKEN')
bot.run(token)
