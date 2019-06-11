# Work with Python 3.6
import discord
from random import randint
import glob
import pandas as pd
from datetime import datetime

from imgurpython import ImgurClient

client_id = '463e415e4ff7895'
client_secret = '314f276c187ac67b5c58b9d6dfbaaa763f0008ca'

klien = ImgurClient(client_id, client_secret)

data = pd.read_csv('file.csv')
data1 = pd.read_csv('bimbing.csv')
TOKEN = 'NTgzMjY4OTExNDg3Nzc4ODE2.XO55jA.2Gp1QefC_3U4K7VwpJIsdTRr-Q0'

client = discord.Client()
swearing = ["kntol","kontol","kntl","kontl","anjing","ajg","bgsd","bgst","bangsat","goblog","gblg","goblok","tai","taek","asu"]


@client.event
async def time():
    flag = 0

    if message.author == client.user:
        return

    if (datetime.now().strftime("%H:%M") == "18:51") and (flag == 0):
        msg = 'HALO'
        flag = 1
        await message.channel.send(msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('halo mbut'):
        msg = ['Bacot kon, {0.author.mention}'.format(message), 'Opo e cuuuuk', 'Opo su', 'GUK!']
        await message.channel.send(msg[randint(0,3)])

    if message.content.lower() in ["bacot","bcd","bacod"]:
        msg = 'Kon sing bacot cuk, {0.author.mention}!'.format(message)
        await message.channel.send(msg)

    if any(x in swearing for x in message.content.lower().split(" ")):
        msg = 'WOY, {0.author.mention}! JANGAN NGOMONG KASAR, BANGSAT!'.format(message)
        await message.channel.send(msg)

    if "wkw" in message.content.lower():
        bauapa = ['TERASI','CALPANAX','MEMEQ','KNALPOT','SAMPAH BANTAR GEBANG','LIMBAH DAUR ULANG']
        msg = '{0.author.mention} KALO KETAWA MULUTNYA BAU {1}!'.format(message, bauapa[randint(0,len(bauapa)-1)])
        await message.channel.send(msg)

    if "kwk" in message.content.lower():
        bauapa = ['TERASI','CALPANAX','MEMEQ','KNALPOT','SAMPAH BANTAR GEBANG','LIMBAH DAUR ULANG']
        msg = '{0.author.mention} KALO KETAWA MULUTNYA BAU {1}!'.format(message, bauapa[randint(0,len(bauapa)-1)])
        await message.channel.send(msg)

    if "kirim meme" in message.content.lower():
        items = klien.subreddit_gallery('indonesia', sort='time', window='year', page=randint(0,4))
        pilih = randint(0,99)
        msg = items[pilih].link
        while (msg.endswith(".jpg") or msg.endswith(".png")) == False :
            pilih = randint(0,99)
            msg = items[pilih].link
        embed=discord.Embed(title=items[pilih].title, url=msg)
        embed.set_image(url=msg)
        await message.channel.send(embed=embed)

    if message.content.lower().startswith('pls play '):
        penak = ['campursari~', 'didi kempot screamo!', 'takbiran remix lah...', 'arif alfiansyah coy']
        msg = 'Mantep cuk, muter {0}! Tapi penak {1}'.format(message.content[9:], penak[randint(0,2)])
        await message.channel.send(msg)

    if message.content.lower().startswith('twit kaesang'):
        pilih = randint(0, len(data)-1)
        embed=discord.Embed(title="Kaesang Pangarep", url=data.link[pilih], description=data.tweet[pilih])
        await message.channel.send(embed=embed)

    if message.content.lower().startswith('dosbingmu'):
        pilih = randint(0, len(data1)-1)
        embed=discord.Embed(title="PEMBIMBINGUTAMA", url=data1.link[pilih], description=data1.tweet[pilih])
        await message.channel.send(embed=embed)

    if "kirim twit" in message.content.lower():
        listfile = glob.glob('drama.sosialmedia/*.jpg')
        await message.channel.send(file=discord.File(listfile[randint(0,len(listfile)-1)]))

    if "tebak angka" in message.content.lower():
        await message.channel.send('Tebak angka dari 1 sampai 10')

        def guess_check(m):
            return m.content.isdigit() and m.author == message.author

        guess = await client.wait_for('jawab', timeout=5, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'GOBLOG KAGA ADA YANG JAWAB! Jawabannya mah {}.'
            await message.channel.send(fmt.format(answer))
            return
        if int(guess.content) == answer:
            await message.channel.send('Anjir, kok lu bener sih')
        else:
            await message.channel.send('GOBLOG EUY, yang bener mah {}.'.format(answer))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(time())

client.run(TOKEN)
