# -*- coding: utf-8 -*-
import discord
import logging
import bot_login
#import lewd
import lewd_args
import asyncio
import random
import rand_choice
import fleentstones
import twitch_emote
import testing
logging.basicConfig(level=logging.INFO)

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
    print('logged in as Sui')
    print(client.user.name)
    print(client.user.id)

@client.event
@asyncio.coroutine
def on_message(message):
    if message.author == client.user:
        return
    if message.server:
        print('message received from', message.channel,"by",message.author,"in", message.server.id)
    else:
        print('message received from', message.channel,"by",message.author)
    try:
        print(message.content)# testing emojis
    except:
        print(message.content.encode("utf-8"))
    # if message.content.startswith('!test'):
    #     yield from client.send_message(message.channel, testing.hangman())
    if message.content.startswith('!sin'):
        yield from client.send_message(message.channel, "I hate sin")

    if message.content.startswith('!lewd'):
        args = message.content.split(' ')
        yield from client.send_message(message.channel,lewd_args.default(args))

    if message.content.startswith('!sui'):
        yield from client.send_message(message.channel,"http://puu.sh/otn07/1209092f05.jpg")

    if message.content.startswith('!poke'):
        yield from client.send_message(message.channel,"hey! stop that {0.author.mention}".format(message))

    if message.content.startswith('!bitchassnigga'):
        yield from client.send_message(message.channel,"fuck off " + message.author.mention)

    if message.content.startswith('!choose') or message.content.startswith('!choice') :
        yield from client.send_message(message.channel,message.author.mention+"  "+rand_choice.choose(message.content))

    if message.content.startswith('!granddad'):
        yield from client.send_message(message.channel,fleentstones.granddad)

    if message.content.startswith('!salt'):
        yield from client.send_message(message.channel,fleentstones.salt)

    if "dank" in message.content.lower():
        yield from client.send_message(message.channel,fleentstones.dank)

    if "sui" in message.content.lower():
        sui_reply = ['huh?', 'ehh?', 'hmm?', 'hah?', 'eh?']
        yield from client.send_message(message.channel,random.choice(sui_reply))

    if "stfu" in message.content.lower():
        yield from client.send_message(message.channel,'no you!')

    if message.content.startswith('!list'):
        memberslist = message.server.members
        onlinemembers = []
        print('listing members')
        for member in memberslist:
            try:
                print('{0}: {1}'.format(str(member).encode("utf-8"),member.id))
            except UnicodeEncodeError:
                print("unicode error")

            if member.status == discord.Status.online:
                # print(member.status)
                onlinemembers.append(member)
        print(len(onlinemembers))
        # yield from client.send_message(message.channel,'listing online users!')
        printstring = 'listing online users!\n'
        for member in onlinemembers:
            printstring += str(member)+" : "+str(member.id) + "\n"
        yield from client.send_message(message.channel, printstring)
        # yield from client.send_message(message.channel,'listing online users!')
#testing
    if message.content.startswith('!channels'):
        channelslist = message.server.channels
        printstring = ""
        file = open('test.txt', 'ab')
        for channel in channelslist:
            try:
                print('{0}: {1}'.format(str(channel).encode("utf-8"),channel.id))
            except UnicodeEncodeError:
                print("unicode error")
            printstring += str(channel)+" : "+str(channel.id) + "\n"
            file.write(str(channel).encode("utf-8")+'\n'.encode("utf-8"))
        yield from client.send_message(message.channel, printstring)

    if message.content.startswith('!randmember'):
        yield from client.send_message(message.channel, str(random.choice(list(message.server.members))))

    if message.content.startswith('!twitch'):
        args = message.content[7:].strip().split(" ")
        print(args)
        if len(args) == 2:
            yield from client.send_file(message.channel, twitch_emote.twitch_emote(args[0],args[1]))
        else:
            yield from client.send_file(message.channel, twitch_emote.twitch_emote(args[0]))
#################

    if message.content.startswith('!giveup'):
        yield from client.send_message(message.channel,'ＮＥＶＥＲ ＧＩＶＥ ＵＰ')

    if message.content.startswith('!howard'):
        yield from client.send_message(message.channel,'http://puu.sh/oFvXh/c73ed52869.jpg')

#inside jokes
    if "justice" in message.content.lower():
        yield from client.send_message(message.channel,'http://media.cleveland.com/books_impact/photo/justicejpg-a19610f0697fbc7a.jpg')

    if "engineer" in message.content.lower():
        yield from client.send_message(message.channel,'no prestige!')

    if "clown" in message.content.lower():
        yield from client.send_message(message.channel,'( ͡° ͜◯ ͡°) ＣＬＯＷＮ ＦＩＥＳＴＡ ( ͡° ͜◯ ͡°) ')

    if message.content.startswith("!paulson"):
        shitpaulsonsays = ['same','tfti',"cuz im a deadchampion","k",'hon hon baguette','what']
        yield from client.send_message(message.channel,random.choice(shitpaulsonsays))#,tts=True)

    if "china" in message.content.lower() or ":flag_cn:" in message.content.lower():
        yield from client.send_message(message.channel,'F U C K  C H I N A')

    # if "darren" in message.content.lower():
    #     yield from client.send_message(message.channel,'thug lyfe')

    # if message.content.startswith('!ogre'):
    #     yield from client.send_message(message.channel,fleentstones.ogre)

    # if message.content == '(╯°□°）╯︵ ┻━┻':
    #     yield from client.send_message(message.channel,'┬──┬ノ( º _ ºノ)')

    # #(ง ͠° ل͜ °)ง

    # if message.content.startswith('!killsui'):
    #     print('test')
    #     yield from client.send_message(message.channel,"I'll be back!")
    #     client.logout()
    #     client.close()
    #     quit()

client.run(bot_login.user,bot_login.password)
# client.run(bot_login.bot_token)

print('*************************************')
print('script arrived here')
print('*************************************')
client.run(bot_login.user,bot_login.password)
print('*************************************')
print('script arrived here2')
print('*************************************')