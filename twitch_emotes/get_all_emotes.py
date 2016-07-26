import urllib.request
from bs4 import BeautifulSoup



# EXAMPLE of downloading an image
# urllib.request.urlretrieve('https://static-cdn.jtvnw.net/emoticons/v1/4337/1.0', 'YouWHY.png')
# NOTE: if you want bigger images, you want to change size "1.0" to 2.0 or 3.0
# I ignored the rest of the stupid Robot Emotes and Turbo Emotes

def download_special_turbo_emotes(size):
    size = str(size)+'.0'
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/2867/"+size, 'KappaHD.png')
    urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/2868/"+size, 'MiniK.png')
    # urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62837/"+size, 'imGlitch.png')
    # urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62841/"+size, 'copyThis.png')
    # urllib.request.urlretrieve("https://static-cdn.jtvnw.net/emoticons/v1/62842/"+size, 'pastaThat.png')


def download_face_emotes(size):
    size = str(size)+'.0'
    url = "https://twitchemotes.com"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    for divs in soup.find_all('img',):
        # print(divs.attrs)
        if divs.get('data-tooltip'):
            img_link = divs.get('src')[:-3]
            emoticon_name = divs.get('data-regex')
            # emoticon_name = divs.get('data-tooltip')[8:-9]
            print(img_link+size,emoticon_name)
            urllib.request.urlretrieve(img_link+size, emoticon_name+'.png')

import requests

def download_bttv_emotes(size):
    betterttv_json_url = requests.get('https://api.betterttv.net/emotes')
    betterttv_json_data = betterttv_json_url.json()

    for emote in betterttv_json_data['emotes']:
        # print(emote)
        bttv_emote_url = 'https:'+emote['url'][:-2]+size+'x'
        bttv_emotename = emote['regex'].strip(')(')
        bttv_emote_filename = bttv_emotename + '.' + emote['imageType']
        try:
            urllib.request.urlretrieve(bttv_emote_url, bttv_emote_filename)
            print(bttv_emote_url, bttv_emote_filename)
        except:
            pass
    # special emotes containing :
    urllib.request.urlretrieve('https://cdn.betterttv.net/emote/54fa8f1401e468494b85b537/'+size+'x', 'trollface.png') # :tf:
    urllib.request.urlretrieve('https://cdn.betterttv.net/emote/55028cd2135896936880fdd7/'+size+'x', 'sad.png') # D:


#########################
# start of code
#########################

# size = 1
#
# download_special_turbo_emotes(size)
# download_face_emotes(size)
# download_bttv_emotes(size)
