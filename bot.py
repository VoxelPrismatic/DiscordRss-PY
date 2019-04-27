from feedy import Feedy
import discord
from discord.ext.commands import Bot
bot = discord.commands()
app = Feedy('feedy.dat')
@app.add('rss feed goes here')
async def rss(info, body):
    channel = bot.get_channel(channel id goes here)
    await channel.send(f"POST // {info['article_url']}")
if __name__ == '__main__':
    app.run()
bot.run('client secret')
