import sys
import os.path


def twitch_emote(emote = "", size = '1.0'):
    abs_path = os.path.abspath(sys.argv[0])
    current_dir = os.path.dirname(abs_path)
    test_dir = os.path.abspath('') #os.getcwd() #bad take out later
    if size.lower() == 'medium' or size.lower() == 'm' or size.lower() == 'mid' or size.lower() == 'med':
        size = '2.0'
    elif size.lower() == 'large' or size.lower() == 'l' or size.lower() == 'big':
        size = '3.0'
    else:
        size = '1.0'
    emote_path = current_dir+'/twitch_emotes/'+size+'/'+emote+'.jpg'
    emote_path = os.path.normpath(emote_path)
    print("argv: "+sys.argv[0])
    print("cur dir: "+test_dir)
    print("emote path: "+emote_path)	
    if os.path.isfile(emote_path):
        return emote_path
    else:
        return (emote+" emote not found!\nplease use a vaild face emote from <https://twitchemotes.com>").strip()

# args = ['f']
# print(twitch_emote(args[0]))
# print(twitch_emote('stinkychfeese','medium'))
