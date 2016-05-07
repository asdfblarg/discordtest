import sys
import os.path


def twitch_emote(emote, size = '1.0'):
    current_dir = os.path.dirname(sys.argv[0])
    if size.lower() == 'medium' or size.lower() == 'm' or size.lower() == 'mid' or size.lower() == 'med':
        size = '2.0'
    if size.lower() == 'large' or size.lower() == 'l' or size.lower() == 'big':
        size = '3.0'
    emote_path = current_dir+'/twitch_emotes/'+size+'/'+emote+'.jpg'
    if os.path.isfile(emote_path):
        return emote_path
    else:
        return "Emote not found!\nPlease use a vaild face emote from https://twitchemotes.com"

print(twitch_emote('stinkychfeese','medium'))